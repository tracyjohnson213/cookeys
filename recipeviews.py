from __main__ import app, mongo, math, render_template, redirect, url_for, request, ObjectId, datetime


""" local variables """
recipesPerPage = 9
categoriesPerPage = 12


def getNumberOfRecipePages(count):
    """ calculate for number of recipe pages required to display results """
    return math.ceil(count/recipesPerPage)

def getcookie(cookie_name):
    """ collect recipe to be displayed by name """
    return mongo.db.recipes.find_one({'cookie_name': cookie_name})


def getrecipe(recipe_id):
    """ collect recipe to be displayed by _id """
    return mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})


def getpageofrecipes(currentpage):
    """ collect recipes to be displayed by page number """
    return mongo.db.recipes.find().skip(recipesPerPage*(int(currentpage)-1))


def getallrecipes():
    """ return all recipes in db """
    return mongo.db.recipes.find()
    
    
def countallrecipes():
    """ return count of all recipes in db """
    return mongo.db.recipes.count_documents({})


def getrecipesincategory(category, currentpage):
    """ collect recipes to be displayed by selected category """
    return mongo.db.recipes.find({'recipe_category': category}).skip(categoriesPerPage*(int(currentpage)-1))


def countrecipesincategory(category):
    """ return count of recipes to be displayed by selected category """
    return mongo.db.recipes.count_documents({'recipe_category': category})


def getallcategories():
    """ return all categories in db """
    return mongo.db.categories.find()


def countallcategories():
    """ return count of all categories in db """
    return mongo.db.categories.count_documents({})


def getallusers():
    """ return all users in db """
    return mongo.db.users.find()


def getallbakeware():
    """ return all bakeware in db """
    return mongo.db.bakeware.find()


@app.route('/')
@app.route('/get_recipes')
@app.route('/get_recipes/<currentpage>')
def get_recipes(currentpage=1):
    """ render all recipes with limit per page"""
    return render_template('recipes.html',
                           recipesPerPage=recipesPerPage,
                           currentpage=currentpage,
                           recipes=getpageofrecipes(currentpage),
                           numberOfPages=getNumberOfRecipePages(countallrecipes()),
                           title='Recipes',
                           bakeware=getallbakeware())


@app.route('/get_recipes/<category>/<currentpage>')
def get_recipes_in_category(category,currentpage):
    """ render recipes in individual category """
    return render_template('recipes.html',
                           recipesPerPage=recipesPerPage,
                           currentpage=currentpage,
                           recipes=getrecipesincategory(category,currentpage),
                           itemCount=countrecipesincategory(category),
                           numberOfPages=getNumberOfRecipePages(countallrecipes()),
                           title='Recipes')


@app.route('/get_cookie/<cookie_name>')
def get_cookie(cookie_name):
    """ render individual recipe with categories listed in sidebar"""
    """ TODO - itemCount should be countrecipesincategory(category) """
    return render_template('cookie.html',
                           recipe=getcookie(cookie_name),
                           categories=getallcategories(),
                           itemCount=countallcategories(),
                           users=getallusers())


@app.route('/add_recipe')
def add_recipe():
    """ render form to input new recipe """
    return render_template('addrecipe.html',
                           categories=getallcategories())


@app.route('/insert_recipe', methods=['post'])
def insert_recipe():
    """ insert recipe into database via add recipe form"""
    now = datetime.now()
    recipes = mongo.db.recipes
    if request.method == "post":
        data = request.form.to_dict()
        data['timestamp']= now.strftime('%b %d %Y')
        recipes.insert_one(data)
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """ render form to edit recipe """
    return render_template('editrecipe.html',
                           recipe=getrecipe(recipe_id),
                           categories=getallcategories())


@app.route('/update_recipe/<recipe_id>', methods=['post'])
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
