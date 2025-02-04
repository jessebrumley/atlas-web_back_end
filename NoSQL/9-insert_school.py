#!/usr/bin/env python3
""" Python function inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """ Python function inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: Mongo DB collection
        kwargs: keyword arguements and properties of collection

    Returns:
        pymongo collection obj: collection including new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
