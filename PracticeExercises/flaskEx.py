#! /usr/bin/env python3
# flaskEx.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Website content goes here!'

@app.route('/about/')
def about():
    return 'Website content goes here!'

if __name__=='__main__':
    app.run(debug=True)
