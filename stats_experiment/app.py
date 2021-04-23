import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from helpers import login_required

# Configure application (Configs taken from C$50 Finance)
app = Flask(__name__)

# Ensure templates are auto-reloaded (Configs taken from C$50 Finance)
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)


@app.route("/")
def index():
    return "Yes"
