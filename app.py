#!/usr/local/bin/python3

import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
podname = os.uname()[1]

@app.route("/")
def index():
    return " Container hsw | POD Working : " + podname + " | v=1\n"

@app.route("/test")
def helloworld():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
