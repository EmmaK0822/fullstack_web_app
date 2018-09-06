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
# app.config["MONGO_URI"] = f"mongodb://{dbuser}:{dbpassword}@ds018558.mlab.com:18558/dogpedia"
# mongo = PyMongo(app)

### Option 2. Use pymongo and connect to database
conn = f"mongodb://{dbuser}:{dbpassword}@ds018558.mlab.com:18558/dogpedia"
client = pymongo.MongoClient(conn)
db = client.dogpedia


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
    # breeds = mongo.db.breeds.find_one()['breed']
    breeds = db.breeds.find_one()['breed']
    return jsonify(breeds)


@app.route("/states")
def states():
    # states = mongo.db.pet_stores.find_one()["geo"]
    states = db.pet_stores.find_one()["geo"]
    return jsonify(states)


@app.route("/breed_traits/<breed>")
def breedTraits(breed):
    """Return the traits for a given breed"""
    name = breed
    apt = db.breed_trait.find_one({'breed':breed})['apt_friendly']
    energy = db.breed_trait.find_one({'breed':breed})['energy']
    shedding = db.breed_trait.find_one({'breed':breed})['shedding']
    
    # Create a dictionary entry for each row of metadata information
    breed_traits = {}
    breed_traits["name"] = apt
    breed_traits["energy"] = energy
    breed_traits["shedding"] = shedding
    breed_traits["apt_friendly"] = apt

    return jsonify(breed_traits)


@app.route("/time_money/<breed>")
def inputValues(breed):
    """Return a list of time and money spent on the breed"""
    datas = list(db.time_money.find({'breed': breed}))
    
    time = []
    money = []
    
    for data in datas:
        time.append(data['time'])
        money.append(data['money'])
    
    value = {
        "breed": breed,
        "time": time,
        "money": money
    }

    return jsonify(value)



if __name__ == "__main__":
    app.run(debug=True, port=4996)
