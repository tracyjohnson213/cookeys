from __main__ import app, mongo, math, render_template, redirect, url_for, request, ObjectId, datetime


""" local variables """
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

