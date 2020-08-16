import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from jinja2 import environmentfilter
import math
from datetime import datetime
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myCookeys'
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")
app.secret_key = os.getenv("SECRET_KEY")
mongo = PyMongo(app)

import recipeviews
import categoryviews


@app.route('/about')
def about():
    """ render about page with team members and contact form """
    return render_template('about.html',
                            team=mongo.db.team.find())


@app.route('/bakeware/<bakeware_name>')
def get_bakery(bakeware_name):
    """ render individual bakeware item"""
    the_bakeware = mongo.db.bakeware.find_one(
        {'name': bakeware_name})
    return render_template('bakeware.html',
                           bakery=mongo.db.bakeware.find_one(
                               {'name': bakeware_name}),
                           bakeware=the_bakeware)


if __name__ == '__main__':
    app.run(
        host=os.getenv('IP','0.0.0.0'),
        port=int(os.getenv('PORT', '5000')),
        debug=True
    )
