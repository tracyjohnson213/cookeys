import unittest
import os
from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")
mongo = PyMongo(app)


class APITest(unittest.TestCase):
    API_URL = "https://5000-bec35a3f-2a73-4d52-9097-2c12048237a7.ws-us02.gitpod.io/"


# --- RECIPE TESTS
# GET request to return all recipes
def test_1_get_all_recipes(self):
    r = request.get(APITest.API_URL)
    self.assertEqual(r.status_code, 200)  # ok
    self.assertEqual(len(mongo.db.recipes.find(), 2))


if __name__ == '__main__':
    unittest.main()
