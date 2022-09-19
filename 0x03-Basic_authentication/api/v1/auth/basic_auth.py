#!/usr/bin/env python3
"""File basic_auth that contains class auth"""
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
        """Class BasicAuth inside of file basic_auth"""
        
        def extract_base64_authorization_header(self, authorization_header: str) -> str:
            """returns Base64 part of Authorization header for Basic Authentication"""
            if authorization_header is None:
                return None
            if not isinstance(authorization_header, str):
                return None
            split_header = authorization_header.split(" ")
            if split_header[0] == "Basic":
                return split_header[1]
            else:
                return None
