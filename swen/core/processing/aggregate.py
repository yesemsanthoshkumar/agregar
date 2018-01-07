"""Aggregates documents and extract entities to be stored
"""

from pymongo import MongoClient
import en_core_web_sm as core

MODEL = core.load()
CLIENT = MongoClient("mongodb://127.0.0.1")

DB = CLIENT['news']

class Node():
    """A node representing a token or phrase"""
    def __init__(self, word, children):
        self.word = word
        self.children = list(children)
        self.points_to = []
    def points(self, node):
        """connects the given node"""
        self.points_to.append(node)
    def __repr__(self):
        if len(list(self.children)) != 0:
            return "{parent} -->> {children}".format(parent=self.word, children=self.points_to)
        return "{parent}".format(parent=self.word)

def create_relationship(node):
    """connect related nodes"""
    if len(list(node.children)) > 0:
#         fl.append(node) # Prefix
        for child in node.children:
            intermittent_node = Node(child, child.children)
            path = create_relationship(intermittent_node)
            if path:
                node.points(path)
#         fl.append(node) #Postfix
        return node
    else:
        return node

for col in DB.collection_names():
    for doc in DB[col].find().limit(1):
        parsed = MODEL(doc['content'])
        ents = [(ent, ent.label_) for ent in parsed.ents]
        for sent in parsed.sents:
            print("Sentence: ", sent)
            root_node = Node(sent.root, sent.root.children)
            root_node = create_relationship(root_node)
            print(root_node)
