from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def index():
    return 'Hello, Flask!'


@app.route('/bee')
def bee():
    return 'Flask is nice'
