#!/usr/bin/env python3
"""task 5 task 5 task 5 task 5 task 5"""
from xmlrpc.client import boolean
import bcrypt


def hash_password(password: str) -> bytes:
    """returns salted, hashed password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates that provided password matches hashed password"""
    if (bcrypt.checkpw(password.encode(), hashed_password)):
        return True
    else:
        return False
