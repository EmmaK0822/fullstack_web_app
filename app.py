import os
from config import dbuser, dbpassword

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use pymongo to set up mongo connection and access a database
app.config["MONGO_URI"] = f"mongodb://{dbuser}:{dbpassword}@ds018558.mlab.com:18558/dogpedia"
mongo = PyMongo(app)

@app.route("/")
def learn():
    """Return learn page"""
    return render_template('learn.html')

if __name__ == "__main__":
    app.run()

@app.route("/breeds")
def breeds():
    breeds = mongo.db.breeds.find_one()['breed']
    return jsonify(breeds)

if __name__ == "__main__":
    app.run()
