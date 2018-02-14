"""Filtering documents basesd on the context"""

from elasticsearch import Elasticsearch
import spacy

es = Elasticsearch()
model = spacy.load('en')

def filter_documents(sentence, sort=None):
    """Filters documents based on the given sentence"""
    s_query = {
        'query': {
            "match": {
                "content": sentence
            }
        }
    }
    if sort:
        s_query['sort'] = sort
    results = es.search(index='swen', doc_type='news', body=s_query)
    return results['hits']['hits']

def extract_entities(raw_doc):
    doc = model(raw_doc['content'])
    return [ent for ent in doc.ents]

