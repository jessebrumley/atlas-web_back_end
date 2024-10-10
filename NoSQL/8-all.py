#!/usr/bin/env python3
""" lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    Args:
        mongo_collection: Mongo DB collection

    Returns:
       Empty list or all documents in the MonogoDB collection
    """
    return mongo_collection.find()
