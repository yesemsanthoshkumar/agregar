"""Agregar
----------------------------------------------
A aggregation system that extracts
information from documents
"""

from pymongo import MongoClient

from preprocess import remove_unwanted_symbols, split_sentences, tag_part_of_speech

CLIENT = MongoClient("mongodb://127.0.0.1")

DB = CLIENT['news']

for col in DB.collection_names():
    for doc in DB[col].find():
        doc = remove_unwanted_symbols(doc['content'])
        doc = split_sentences(doc)
        doc = tag_part_of_speech(doc)
        print(doc)
    break
