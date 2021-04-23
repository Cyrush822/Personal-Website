# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))


# app.route("/experiment")
# def index():
#     return "Yes"

# def app(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'It works!\n'
#     version = 'Python v' + sys.version.split()[0] + '\n'
#     response = '\n'.join([message, version])
#     return [response.encode()]

import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

# Configure application (Configs taken from C$50 Finance)
app = Flask(__name__)

# Ensure templates are auto-reloaded (Configs taken from C$50 Finance)
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)


@app.route("/")
def index():
    return "Yes"