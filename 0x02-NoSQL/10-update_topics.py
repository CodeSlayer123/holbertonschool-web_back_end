#!/usr/bin/env python3
"""This is task 10"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """changes all topics of school document based on name"""
    query = {"name": name}
    values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, values)
