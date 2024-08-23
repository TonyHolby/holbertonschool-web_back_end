#!/usr/bin/env python3
"""
    A Python function that changes all topics of a school
    document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
        Changes all topics of a school document based on the name.

        Args:
            mongo_collection: The MongoDB collection.
            name (string): The name of the school to update.
            topic (list of strings): The list of topics to set for the school.

        Returns:
            The result of the update operation.
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

    return result.modified_count
