"""Filtering documents basesd on the context"""

from elasticsearch import Elasticsearch

es = Elasticsearch()

def filter_documents(sentence):
    """Filters documents based on the given sentence"""
    results = es.search(index='swen', doc_type='news', body={
        'query': {
            "match": {
                "content": sentence
            }
        }
    })
    return results
