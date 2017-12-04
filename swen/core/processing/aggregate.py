"""Aggregates documents and extract entities to be stored
"""

from pymongo import MongoClient
from nltk.chunk import ne_chunk

from preprocess import remove_unwanted_symbols, split_sentences, tag_part_of_speech
from inverted_index import InvertedIndex

CLIENT = MongoClient("mongodb://127.0.0.1")

DB = CLIENT['news']

IV = InvertedIndex()

for col in DB.collection_names():
    for doc in DB[col].find().limit(5):
        id = doc['_id']
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
                    IV.add(" ".join([
                        wd
                        for wd, tag in chunk.leaves()
                    ]), id)
        for ent in entities:
            print(ent[0], ent[1], sep='\t')

print(IV.idx)
