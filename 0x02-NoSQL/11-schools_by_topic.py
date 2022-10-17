#!/usr/bin/env python3
"""This is task 11"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """returns list of school having specific topic"""
    docs = []
    cursor = mongo_collection.find({"topics": topic})
    for doc in cursor:
        docs.append(doc)
    return docs
