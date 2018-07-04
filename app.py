#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/contacts")
def contacts():
	return render_template('contacts.html')

@app.route("/reserver")
def reserver():
	return render_template('reserver.html')

@app.route("/medias")
def medias():
	return render_template('medias.html')

@app.route("/restaurant")
def restaurant():
	return render_template('restaurant.html')

@app.route("/infos-pratiques")
def infospratiques():
	return render_template('infos-pratiques.html')


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)