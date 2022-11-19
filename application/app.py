from flask import Flask, render_template
from werkzeug.utils import send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/static/<path:filepath>')
def routeto():
    return send_from_directory('static', filepath)