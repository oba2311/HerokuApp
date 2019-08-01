from flask import FLASK

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>yo yo yooo</h1>'
