#!/usr/bin/env python3
"""File auth that contains class auth"""
from flask import request
from typing import TypeVar, List
import os


class Auth():
    """class Auth inside of file Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method require_auth"""
        if (path is None):
            return True
        if (excluded_paths is None or len(excluded_paths) == 0):
            return True
        if (path in excluded_paths or (path + "/") in excluded_paths):
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method authorization_header"""
        if request is None:
            return None
        if "Authorization" in request.headers:
            return request.headers["Authorization"]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method current_user"""
        return None

    def session_cookie(self, request=None):
        """returns cookie value from request"""
        if request is None:
            return None
        return request.cookies.get(os.getenv("SESSION_NAME"))
