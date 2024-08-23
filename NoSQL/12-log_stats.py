#!/usr/bin/env python3
"""
    A Python script that provides some stats about Nginx logs
    stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
        - Counts the number of documents in this collection.
        - Displays the number of logs.
        - Counts the number of documents for each method.
        - Counts the number of documents with method GET and path /status.
        - Displays the number of checked status.
    """
    client = MongoClient('mongodb://localhost:27017/')

    the_logs_database = client.logs
    collection = the_logs_database.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_count} status check")
