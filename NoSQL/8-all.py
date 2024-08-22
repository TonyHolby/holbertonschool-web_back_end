#!/usr/bin/env python3
""" A Python function that lists all documents in a collection. """


def list_all(mongo_collection):
    """
        Lists all documents in a collection.

        Args:
            mongo_collection: The MongoDB collection.

        Returns:
            A list of all documents in the collection.
            If no documents, return an empty list.
    """
    all_documents = mongo_collection.find()
    list_of_documents = list(all_documents)

    return list_of_documents
