import re
import json
import operator
import json
from collections import Counter
from nltk.corpus import stopwords
import string
import nltk

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


nltk.download("stopwords") # download the stopword corpus on our computer
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT']


fname = 'ArtificialIntelligenceTweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    count_hash = Counter()
    count_only = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
        terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#', '@'))]
        count_all.update(terms_stop)
        count_hash.update(terms_hash)
        count_only.update(terms_only)
    print("The top ten most frequent tokens")
    for word, index in count_all.most_common(10):
        print ('%s : %s' % (word, index))

    print("\nThe top ten most frequent hashtags")
    for word, index in  count_hash.most_common(10):
        print ('%s : %s' % (word, index))

    print("\nThe top ten most frequent terms, skipping mentions and hashtags")
    for word, index in count_only.most_common(10):
        print ('%s : %s' % (word, index))
