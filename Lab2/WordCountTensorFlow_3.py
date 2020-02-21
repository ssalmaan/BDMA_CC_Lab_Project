import nltk
nltk.download('stopwords')
import re

from collections import Counter
from nltk.corpus import stopwords

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    lowers = text.lower()
    no_punctuation = re.sub(r'[^\w\s]','',lowers)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
# the lambda expression below this comment
# stores stopwords in a variable for eficiency: 
# it avoids retrieving them from ntlk for each iteration
sw = stopwords.words('english')
filtered = [w for w in tokens if not w in sw]
count = Counter(filtered)
print "Top 10 common words and respective counts without punctuations and after removing stop words:" 
print (count.most_common(10))
print "Total number of words from the book without punctuations and after removing stop words:" 
print (len(count))
