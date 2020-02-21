import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import re
import string
import nltk
from collections import Counter
from nltk.corpus import stopwords

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'rt', 'iphone']

fname = 'Iphone.json'


with open(fname, 'r') as f:
    count_all  =Counter()
    count_battery = Counter()
    count_camera = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_hash = [term for term in preprocess(tweet['text'].lower()) if term not in stop]
        count_all.update(terms_hash)
        if 'battery' in tweet['text']:
            count_battery.update(terms_hash)
        if 'camera' in tweet['text']:
            count_camera.update(terms_hash)
# Print the first 10 most frequent words
print(count_all.most_common(10))
print("Most frequent terms in tweets containing 'camera'")
print(count_battery.most_common(10))
print("Most frequent terms in tweets containing 'battery'")
print(count_camera.most_common(10))
