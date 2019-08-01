from flask import FLASK

app = FLASK(__name__)

@app.route('/')
def index():
    return '<h1>yo yo yooo</h1>'
