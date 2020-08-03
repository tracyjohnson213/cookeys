import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myCookeys'
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    """ render all recipes """
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find(),
                           title='Recipes')


if __name__ == '__main__':
    app.run(
        debug=True
    )
