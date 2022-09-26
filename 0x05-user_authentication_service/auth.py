#!/usr/bin/env python3
"""Auth file for mysql"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from user import User


def _hash_password(password: str) -> bytes:
        """returns input password hashed with bcrypt.hashpw"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed


def _generate_uuid() -> str:
    """return string representation of new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User", email, "already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """validates login with email and password"""
        try:
            user = self._db.find_user_by(email=email)
            hashed = user.hashed_password
            return bcrypt.checkpw(password.encode(), hashed)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """finds user, generates new UUID and stores it
        in database and returns session ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return uuid
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """returns user from given session_id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroy session, updates user session_id to None"""
        if user_id is None:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
            return None
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """generates UUID and updates user's reset_token database field"""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """updates password from given reset_token and password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=hashed_password,
                                 reset_token=None)

        except Exception:
            raise ValueError
