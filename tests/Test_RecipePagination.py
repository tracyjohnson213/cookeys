# verify class disabled for previous button when currentpage = 1
# verify class disabled for next button when currentpage = numberOfPages
# verify class active pageNumber when currentpage = pageNumber
# verify result of clicking previous button displays currentpage -1
# verify result of clicking next button displays currentpage +1
# verify result displayed when random pageNumber clicked
# verify numberOfPages = math.ceil(resultsCount/recipesPerPage)
# verify number of items displayed <= recipesPerPage

import os
from flask import Flask
import math

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myCookeys'
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")
mongo = PyMongo(app)
recipesPerPage = 9
categoriesPerPage = 12
recipe_count = mongo.db.recipes.count_documents({})
category_count = mongo.db.categories.count_documents({})


def get_number_of_pages(self):
    self.assertEqual(math.ceil(recipe_count/recipesPerPage),2)
