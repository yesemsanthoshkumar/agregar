"""Functions for the flow of messages"""

from .preprocess import split_sentences, remove_unwanted_symbols, tag_part_of_speech

def reply(value):
    """
    1. Gets a message
    2. Process the message
    3. Sends a reply
    """
    sents = [
        remove_unwanted_symbols(
            sent
        )
        for sent in split_sentences(value['msg'])
    ]
    ents = " ".join(
        [
            x[0]
            for sent in tag_part_of_speech(sents)
            for x in sent
        ]
    )
    return {
        "msg": ents
    }
