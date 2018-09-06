import os
from config import dbuser, dbpassword

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)

# 1. Database setup

### Option 1. Use flask_pymongo to set up mongo connection and access a database
app.config["MONGO_URI"] = f"mongodb://{dbuser}:{dbpassword}@ds018558.mlab.com:18558/dogpedia"
mongo = PyMongo(app)

### Option 2. Use pymongo and connect to database
# conn = f"mongodb://{dbuser}:{dbpassword}@ds018558.mlab.com:18558/dogpedia"
# client = pymongo.MongoClient(conn)
# db = client.dogpedia
# collection_breeds = db.breeds
# collection_pet_stores = db.pet_stores


# 2. Setting up the basic template route

@app.route("/")
def index():
    """Return index page"""
    return render_template('index.html')

@app.route("/find")
def find():
    """Return find page"""
    return render_template('find.html')

@app.route("/learn")
def learn():
    """Return learn page"""
    return render_template('learn.html')

@app.route("/adopt")
def adopt():
    """Return adopt page"""
    return render_template('adopt.html')


# 3. Getting extra info with additional route

@app.route("/breeds")
def breeds():
    breeds = mongo.db.breeds.find_one()['breed']
    # breeds = collection_breeds.find_one()
    return jsonify(breeds)


@app.route("/states")
def states():
    states = mongo.db.pet_stores.find_one()["geo"]
    # states = collection_pet_stores.find_one()
    return jsonify(states)

@app.route("/breed_traits/<breed>")
def breedTraits(breed):
    """Return the traits for a given breed"""
    name = breed
    apt = mongo.db.breed_trait.find_one({'breed':breed})['apt_friendly']
    energy = mongo.db.breed_trait.find_one({'breed':breed})['energy']
    shedding = mongo.db.breed_trait.find_one({'breed':breed})['shedding']
    
    # Create a dictionary entry for each row of metadata information
    breed_traits = {}
    breed_traits["name"] = apt
    breed_traits["energy"] = energy
    breed_traits["shedding"] = shedding
    breed_traits["apt_friendly"] = apt

    return jsonify(breed_traits)


if __name__ == "__main__":
    app.run(debug=True, port=4996)
