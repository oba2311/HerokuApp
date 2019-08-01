from flask import Flask

app = Flask()

@app.route('/')
def index():
    return '<h1>yo yo yooo</h1>'
