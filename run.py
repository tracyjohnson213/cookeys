import os
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import math

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myCookeys'
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")

mongo = PyMongo(app)
recipesPerPage = 9
recipe_count = mongo.db.recipes.count()


def getNumberOfPages(count):
    return math.ceil(count/recipesPerPage)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    """ render all recipes """
    currentpage = 1
    pagelessone = int(currentpage)-1
    return render_template('recipes.html',
                           recipesPerPage=recipesPerPage,
                           currentpage=1,
                           recipes=mongo.db.recipes.find().skip(recipesPerPage*(pagelessone)),
                           numberOfPages=getNumberOfPages(recipe_count),
                           title='Recipes')


@app.route('/get_recipes/<currentpage>')
def get_recipes_set(currentpage):
    """ render specific set of recipes """
    pagelessone = int(currentpage)-1
    return render_template('recipes.html',
                           recipesPerPage=recipesPerPage,
                           currentpage=currentpage,
                           recipes=mongo.db.recipes.find().skip(recipesPerPage*(pagelessone)),
                           numberOfPages=getNumberOfPages(recipe_count),
                           title='Recipes')


@app.route('/get_recipes/<currentpage>')
def get_next_page(currentpage):
    newcurrentpage = int(currentpage) - 1
    return redirect(url_for('get_recipes_set',
                            currentpage=newcurrentpage),
                    recipesPerPage=recipesPerPage)


@app.route('/get_recipes/<currentpage>')
def get_prev_page(currentpage):
    newcurrentpage = int(currentpage) + 1
    return redirect(url_for('get_recipes_set',
                            currentpage=newcurrentpage),
                    recipesPerPage=recipesPerPage)


@app.route('/get_cookie/<cookie_name>')
def get_cookie(cookie_name):
    """ render individual recipe """
    the_cookie = mongo.db.recipes.find_one(
        {"cookie_name": cookie_name})
    return render_template('cookie.html',
                           recipe=mongo.db.recipes.find_one(
                               {'cookie_name': cookie_name}),
                           cookie=the_cookie,
                           categories=mongo.db.categories.find())


@app.route('/get_categories')
def get_categories():
    """ render all categories """
    return render_template('categories.html',
                           categories=mongo.db.categories.find(),
                           title='Categories')


if __name__ == '__main__':
    app.run(
        debug=True
    )
