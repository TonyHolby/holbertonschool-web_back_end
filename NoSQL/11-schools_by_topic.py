#!/usr/bin/env python3
"""
    A Python function that returns the list of school
    having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
        Lists the school having a specific topic.

        Args:
            mongo_collection: The MongoDB collection.
            topic (string): The list of topics to set for the school.

        Returns:
            The list of school having a specific topic.
    """
    all_documents = mongo_collection.find({"topics": topic})
    list_of_documents = list(all_documents)

    return list_of_documents
