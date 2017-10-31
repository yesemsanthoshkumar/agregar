"""Preprocessing utilities for documents"""

import re
from nltk import pos_tag

def split_sentences(doc):
    """Split paragraphs into separate sentences
    """
    return doc.split('.')

def remove_unwanted_symbols(doc):
    """Removes unwanted symbols other than
    alpha numerics

    Parameters
    ----------
    doc     :   string
        Document
    """
    doc = re.sub("[^A-Za-z0-9\.]", " ", doc)
    return re.sub("\s+", " ", doc)

def tag_part_of_speech(sentences):
    """Tags Parts of speech for the given sentences

    Parameters
    ----------
    sentences   :   list
        List of sentences belonging to a document
    """
    for sentence in sentences:
        yield pos_tag(sentence.split())
