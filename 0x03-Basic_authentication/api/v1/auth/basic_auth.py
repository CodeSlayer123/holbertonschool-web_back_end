#!/usr/bin/env python3
"""File basic_auth that contains class auth"""
from flask import request
from typing import TypeVar, List, Tuple
from api.v1.auth.auth import Auth
import base64

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

        def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
            """returns decoded value of a Base64 string"""
            if base64_authorization_header is None:
                return None
            if not isinstance(base64_authorization_header, str):
                return None
            try:
                return base64.b64decode(base64_authorization_header).decode('utf-8')
            except Exception:
                return None

        def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
            """returns user email and password from Base64 decoded value"""
            if decoded_base64_authorization_header is None:
                return (None, None)
            if not isinstance(decoded_base64_authorization_header, str):
                return (None, None)
            if ":" not in decoded_base64_authorization_header:
                return (None, None)
            return decoded_base64_authorization_header.split(":")
