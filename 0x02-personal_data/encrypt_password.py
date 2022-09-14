#!/usr/bin/env python3
"""task 5 task 5 task 5 task 5 task 5"""
from xmlrpc.client import boolean
import bcrypt

def hash_password(password: str) -> bytes:
    """returns salted, hashed password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def is_valid(hashed_password:bytes, password: str) -> bool:
    if (bcrypt.hashpw(password, hashed_password) == hashed_password):
        return True
    else:
        return False
