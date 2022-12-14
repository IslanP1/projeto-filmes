from flask import Flask
from main import app

@app.route('/')
def index():
    return 'Hello world!'