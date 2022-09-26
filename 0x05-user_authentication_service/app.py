#!/usr/bin/env python3
"""app file to set up Flask app"""
import bcrypt
from db import DB
from user import User
from flask import Flask, request, abort, jsonify
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
    except:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")