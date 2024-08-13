#!/usr/bin/env pythont
"""ask 8"""


def list_all(mongo_collection):
    """Lists all docments in a collection """
    return [doc for doc in mongo_collection.find()]

