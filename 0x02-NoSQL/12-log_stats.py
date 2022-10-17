#!/usr/bin/env python3
"""This is task 12"""
from pymongo import MongoClient


def log_stats(mongo_collection, topic):
    """provides stats about Nginx logs stored in MongoDB"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient()
    db = client.logs
    collection = db.nginx
    all_collections = collection.count_documents()
    print(f"{all_collections} logs")
    print("Methods:")
    for meth in methods:
        query = {"method":meth }
        print(f"\tmethod {meth}: {collection.find(query).count()}")
    status_query = {"method":meth[0], 'path': '/status'}
    print(f"{collection.find(status_query).count()} status check")

if __name__ == "__main__":
    log_stats()
