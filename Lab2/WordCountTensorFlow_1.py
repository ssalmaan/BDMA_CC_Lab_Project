import nltk
nltk.download('punkt') 
import re

from collections import Counter

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    tokens = nltk.word_tokenize(text)
    return tokens

tokens = get_tokens()
count = Counter(tokens)
print "Top 10 common words and respective counts :" 
print (count.most_common(10))
print "Total number of words of the book:" 
print (len(tokens))