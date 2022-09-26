#!/usr/bin/env python3
"""app file to set up Flask app"""
import bcrypt
from db import DB
from user import User
from flask import Flask, request, abort, jsonify, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def start_up():
    """returns JSON payload of form"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def register():
    """implements POST /users route"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def login():
    """logs in to session"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.valid_login(email=email, password=password)
        session_id = AUTH.create_session(email=email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    except Exception:
        abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout():
    """logs out of session"""
    session_id = request.cookies.get("session_id")
    try:
        AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(session_id)
        return redirect("/")
    except Exception:
        abort(403)


@app.route("/profile", methods=['GET'])
def profile():
    """gets profile of a user from session_id cookie"""
    session_id = request.cookies.get("session_id")
    try:
        user = AUTH.get_user_from_session_id(session_id)
        return jsonify({"email": user.email}), 200
    except Exception:
        abort(403)


@app.route("/reset_password", methods=['POST'])
def get_reset_password_token():
    """resets the password token"""
    try:
        email = request.form.get("email")
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except Exception:
        abort(403)


@app.route("/reset_password", methods=['PUT'])
def update_password():
    """updates the password token"""
    try:
        email = request.form.get("email")
        reset_token = request.form.get("reset_token")
        new_password = request.form.get("new_password")
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
