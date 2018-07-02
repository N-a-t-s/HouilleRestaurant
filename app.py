#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/home")
def home():
	return render_template('home.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)