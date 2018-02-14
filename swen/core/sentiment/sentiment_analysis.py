"""Sentiment analysis section"""

from extractor import filter_documents
from collections import Counter

import matplotlib.pyplot as mplt

def get_words(pos=True):
    f_name = "positive.txt" if pos else "negative.txt"
    words = []
    with open(("swen/core/sentiment/" + f_name)) as fp:
        for line in fp.readline():
            if line.startswith(";"):
                pass
            words.append(line.strip())
    return words

def sentiment_over_time(sentence):
    """Plots sentiment over time period for the topic or entities
    given"""
    positive = get_words()
    negative = get_words(pos=False)
    docs = filter_documents(sentence, sort=[
        {
            "date": {
                "order": "asc"
            }
        }
    ])
    print("Got ", len(docs), " docs")
    dates = []
    sentiment = []
    for doc in docs:
        dates.append(doc['_source']['date'])
        tokens = Counter(doc['_source']['content'].replace(".", ' ').split())
        doc_sentiment = 0
        for tok in tokens:
            if tok in positive:
                doc_sentiment = doc_sentiment + (tokens[tok] * 1)
            elif tok in negative:
                doc_sentiment = doc_sentiment + (tokens[tok] * -1)
        sentiment.append(doc_sentiment)
    # print(dates, sentiment)
    x = list(range(len(dates)))
    mplt.plot(x, sentiment)
    # mplt.xticks(x, dates)
    mplt.show()
