#!/usr/bin/env python3
"""File session_auth that contains class SessionAuth"""
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from api.v1.views import app_views


class SessionAuth(Auth):
    """class SessionAuth inside of file session_auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates Session ID for user_id"""
        if user_id is None or not isinstance(user_id, str):
            None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns User ID based on Session ID"""
        if session_id is None or not isinstance(session_id, str):
            None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns User instance based on cookie value"""
        return User.get(
            self.user_id_for_session_id(
                self.session_cookie(request)))

    def destroy_session(self, request=None):
        """deletes user session / logout"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
