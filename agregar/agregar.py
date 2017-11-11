"""Agregar
----------------------------------------------
A aggregation system that extracts
information from documents
"""

from pymongo import MongoClient
from nltk.chunk import ne_chunk

from preprocess import remove_unwanted_symbols, split_sentences, tag_part_of_speech

CLIENT = MongoClient("mongodb://127.0.0.1")

DB = CLIENT['news']

for col in DB.collection_names():
    for doc in DB[col].find():
        entities = []
        doc = remove_unwanted_symbols(doc['content'])
        doc = split_sentences(doc)
        doc = tag_part_of_speech(doc)
        for sent in doc:
            for chunk in ne_chunk(sent):
                if hasattr(chunk, 'label'):
                    entities.append(
                        (
                            " ".join([
                                wd
                                for wd, tag in chunk.leaves()
                            ]),
                            chunk.label()
                        )
                    )
        for ent in entities:
            print(ent[0], ent[1], sep='\t')
