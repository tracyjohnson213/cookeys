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

""" local variables """
mongo = PyMongo(app)
recipesPerPage = 9
categoriesPerPage = 12
recipe_count = mongo.db.recipes.count_documents({})
category_count = mongo.db.categories.count_documents({})
company = mongo.db.company.find()


def getNumberOfPages(count):
    """ calculate for number of pages required to display results """
    return math.ceil(count/recipesPerPage)


def getItemCount(category):
    return mongo.db.categories.count_documents({'recipe_category': category})


@app.route('/')
@app.route('/get_recipes')
@app.route('/get_recipes/<currentpage>')
def get_recipes(currentpage=1):
    """ render all recipes with limit per page"""
    numberOfPages = getNumberOfPages(recipe_count)
    return render_template('recipes.html',
                           recipesPerPage=recipesPerPage,
                           currentpage=currentpage,
                           recipes=mongo.db.recipes.find()
                           .skip(recipesPerPage*(int(currentpage)-1)),
                           numberOfPages=numberOfPages,
                           title='Recipes')


@app.route('/get_recipes/<category>/<currentpage>')
def get_recipes_in_category(category,currentpage):
    """ render recipes in individual category """
    recipe_count = mongo.db.recipes.count_documents({'recipe_category': category})
    numberOfPages = getNumberOfPages(recipe_count)
    return render_template('recipes.html',
                           recipesPerPage=recipesPerPage,
                           currentpage=currentpage,
                           recipes=mongo.db.recipes
                           .find({'recipe_category': category})
                           .skip(categoriesPerPage*(int(currentpage)-1)),
                           itemCount=recipe_count,
                           numberOfPages=numberOfPages,
                           title='Recipes')


@app.route('/get_cookie/<cookie_name>')
def get_cookie(cookie_name):
    """ render individual recipe with categories listed in sidebar"""
    the_cookie = mongo.db.recipes.find_one(
        {"cookie_name": cookie_name})
    return render_template('cookie.html',
                           recipe=mongo.db.recipes.find_one(
                               {'cookie_name': cookie_name}),
                           cookie=the_cookie,
                           categories=mongo.db.categories.find(),
                           itemCount=category_count,
                           users=mongo.db.users.find())


@app.route('/add_recipe')
def add_recipe():
    """ render form to input new recipe """
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """ insert recipe into database via add recipe form"""
    now = datetime.now()
    recipes = mongo.db.recipes
    if request.method == "POST":
        data = request.form.to_dict()
        data['timestamp']= now.strftime('%b %d %Y')
        recipes.insert_one(data)
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """ render form to edit recipe """
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html',
                           recipe=the_recipe,
                           categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    """ update recipe in database via edit recipe form"""
    now = datetime.now()
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        'cookie_name': request.form.get('cookie_name'),
        'ingredients': request.form.get('ingredients'),
        'qty': request.form.get('qty'),
        'steps': request.form.get('steps'),
        'firstname': request.form.get('firstname'),
        'lastname': request.form.get('lastname'),
        'summary': request.form.get('summary'),
        'recipe_category': request.form.get('recipe_category'),
        'image_source': request.form.get('image_source'),
        'timestamp': now.strftime('%b %d %Y')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """ remove recipe from database """
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/get_categories')
@app.route('/get_categories/<currentpage>')
def get_categories(currentpage=1):
    """ render all categories limited by current page"""
    numberOfPages = getNumberOfPages(category_count)
    return render_template('categories.html',
                           categoriesPerPage=categoriesPerPage,
                           currentpage=currentpage,
                           categories=mongo.db.categories.find()
                           .skip(categoriesPerPage*(int(currentpage)-1)),
                           numberOfPages=numberOfPages,
                           title='Categories')


@app.route('/add_category')
def add_category():
    """ render form to input new category """
    return render_template('addcategory.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_category', methods=['POST'])
def insert_category():
    """ insert category into database via add category form"""
    now = datetime.now()
    categories = mongo.db.categories
    if request.method == "POST":
        data = request.form.to_dict()
        data['timestamp'] = now.strftime('%b %d %Y')
        categories.insert_one(data)
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    """ render form to edit category """
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                               {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    """ update category in database via edit category form """
    now = datetime.now()
    mongo.db.categories.update({'_id': ObjectId(category_id)},
                               {
            'recipe_category': request.form.get('recipe_category'),
            'category_desc': request.form.get('category_desc'),
            'timestamp': now.strftime('%b %d %Y')
        })
    return redirect(url_for('get_categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    """ remove category from database """
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/about')
def about():
    """ render about page with team members and contact form """
    return render_template('about.html',
                            team=mongo.db.team.find())


@app.route('/contact', methods=['POST'])
def contact():
    now = datetime.now()
    if request.method == 'POST':
        data = request.form.to_dict()
        data['timestamp'] = now.strftime('%b %d %Y')
    return render_template('contact.html', 
                            data=data)


if __name__ == '__main__':
    app.run(
        host=os.getenv('IP','0.0.0.0'),
        port=int(os.getenv('PORT', '5000')),
        debug=True
    )
