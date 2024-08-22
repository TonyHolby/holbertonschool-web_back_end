#!/usr/bin/env python3
"""
    A Python function that inserts a new document in a
    collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
        Inserts a new document using the provided kwargs.

        Args:
            mongo_collection: The MongoDB collection.

        Returns:
            The id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
