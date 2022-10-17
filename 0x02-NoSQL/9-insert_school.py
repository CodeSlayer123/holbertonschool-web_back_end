#!/usr/bin/env python3
"""This is task 9"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ inserts new document in collection based on kwargs"""
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
