#!/usr/bin/env python3
"""This is task 8"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    all_docs = []
    cursor = mongo_collection.find()
    for doc in cursor:
        all_docs.append(doc)
    return all_docs
