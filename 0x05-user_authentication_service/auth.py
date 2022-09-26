#!/usr/bin/env python3
"""Auth file for mysql"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from user import User


def _hash_password(password:str) -> bytes:
        """returns salted hash of input password, hashed with bcrypt.hashpw"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed

def _generate_uuid():
    """return string representation of new UUID"""
    return str(uuid.uuid4())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email:str, password: str) -> User:
        """registers user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User", email, "already exists")
        except NoResultFound:
            hashed_password =_hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email, password) -> bool:
        """validates login with email and password"""
        try:
            user = self._db.find_user_by(email=email)
            hashed = user.hashed_password
            return bcrypt.checkpw(password.encode(), hashed)
        except NoResultFound:
            return False

    def create_session(self, email:str) -> str:
        """finds user corresponding to email, generates new UUID and stores it in
        database as user’s session_id and returns session ID"""
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            self._db.update_user(user.id, session_id=uuid)
            return uuid
        except:
            return None

    def get_user_from_session_id(self, session_id:str) -> User:
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id:int) -> None:
        if user_id is None:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
            return None
        except Exception:
            return None
