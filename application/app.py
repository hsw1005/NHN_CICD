#!/usr/local/bin/python3

import os
from flask import Flask, render_template

from werkzeug.utils import send_from_directory

app = Flask(__name__)
podname = os.uname()[1]

# @app.route("/")
# def index():
#     return " Container hsw | POD Working : " + podname + " | v=2\n"


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/static/<path:filepath>')
def routeto():

    return send_from_directory('static', filepath)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
