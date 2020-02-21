from bs4 import BeautifulSoup
import urllib.request
import os
import requests
import shutil
import base64
import googleapiclient.discovery
import matplotlib; matplotlib.use("TkAgg")
import numpy as np
from matplotlib import pyplot as plt ; plt.rcdefaults()


def make_soup(url):
    session = requests.Session()
    html = session.get(url).text
    return BeautifulSoup(html)


def get_histogram(home, page):
    url = home + page
    service = googleapiclient.discovery.build('vision', 'v1')

    soup = make_soup(url)

    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "images found.")
    print ('Downloading images to current working directory.')

    image_links = [each.get('src') for each in images]

    num_images = 0

    tags_dict = {}
    
    if not os.path.exists(page):
        os.makedirs(page)

    for each in image_links:
        try:
            if each is None: 
                continue
            filename = page+"/"+each.split('/')[-1]

            print(each)
            r = requests.get(each, stream=True)
            if r.status_code == 200:
                with open(filename, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                with open(filename, 'rb') as image:
                    image_content = base64.b64encode(image.read())
                    service_request = service.images().annotate(body={
                        'requests': [{
                            'image': {
                                'content': image_content.decode('UTF-8')
                            },
                            'features': [{
                                'type': 'LABEL_DETECTION'
                            }]
                        }]
                    })


                    response = service_request.execute()

                    for result in response['responses'][0]['labelAnnotations']:
                        tag = result['description']
                        if tag in tags_dict.keys():
                            tags_dict[tag] += result['score']
                        else:
                            tags_dict[tag] = result['score']

            num_images += 1 
        except:
            print(each+": not downloaded")
        if num_images==100:
            break

    top_tags_list = sorted(tags_dict.items(), key=lambda x:x[1], reverse=True)[:25]
    labels = [tag for tag, score in top_tags_list]
    index = np.arange(len(labels))
    total_score = [round(score, 2) for tag, score in top_tags_list]

    plt.bar(index, total_score, align='center', alpha=0.5)
    plt.xticks(index, labels, rotation='vertical')
    plt.ylabel('Total Score')
    plt.title(page+': Top 25 tags')
    plt.savefig(page+".png", bbox_inches = "tight")



page = 'WeAreMessi'
# page = 'andresiniesta8'
# page = 'Criterion'
# page = 'janusfilms'
# page = 'lgbtfdn'
get_histogram('https://twitter.com/', page)
