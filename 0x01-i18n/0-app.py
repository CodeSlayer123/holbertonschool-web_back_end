#!/usr/bin/env python3

"""task 0 flask app.py"""
from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def startup():
    """renders 0-index html page"""
    return render_template('0-index.html')



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)