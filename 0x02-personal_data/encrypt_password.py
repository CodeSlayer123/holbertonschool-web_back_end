#!/usr/bin/env python3
"""task 5 task 5 task 5 task 5 task 5"""
import bcrypt
def hash_password(password:str) -> bytes:
    """returns salted, hashed password"""
    return bcrypt.hashpw(password, bcrypt.gensalt())