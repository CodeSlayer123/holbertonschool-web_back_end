#!/usr/bin/env python3
"""File session_auth that contains class SessionAuth"""
from flask import jsonify, request, abort
from typing import TypeVar, List
from itsdangerous import exc
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from api.v1.views import app_views
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def x() -> str:
    """ POST /api/v1/auth_session/login"""
    all_users = [user.to_json() for user in User.all()]
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None or len(email) == 0:
        return {"error": "email missing"}, 400
    if password is None or len(password) == 0:
        return {"error": "password missing"}, 400
    print(email)
    print(password)
    my_user = User.search({"email": email})
    if my_user is None or len(my_user) == 0:
        return {"error": "no user found for this email"}, 404
    if not my_user[0].is_valid_password(password):
        return {"error": "wrong password"}, 401
    from api.v1.app import auth
    result = jsonify(my_user[0].to_json())
    result.set_cookie(os.getenv("SESSION_NAME"),
                      auth.create_session(my_user[0].id))
    return result


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def delete() -> str:
    """ DELETE /api/v1/auth_session/logout"""
    from api.v1.app import auth
    try:
        auth.destroy_session(request)
    except:
        abort(404)
    return jsonify({}), 200
