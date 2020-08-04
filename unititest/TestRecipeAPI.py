import unittest
import os
from flask import Flask, request
from flask_pymongo import PyMongo
import test.data as data

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")
mongo = PyMongo(app)


class APITest(unittest.TestCase):
    API_URL = "https://8080-e6fbbb44-6582-4788-b88f-5b9232d23bb0.ws-us02.gitpod.io/"


# variable for new url with route
def _get_url(self, route):
    return "{}/{}".format(APITest.API_URL, route)


# variable for new url with route and any item;
# replacing whitespace in str(item)
def _get_url_withid(self, route, item):
    return "{}/{}/{}".format(APITest.API_URL, route, item.replace("", "%20"))


# --- RECIPE TESTS
# GET request to return all recipes
def test_1_get_all_recipes(self):
    r = request.get(APITest.API_URL)
    self.assertEqual(r.status_code, 200)  # ok
    self.assertEqual(len(mongo.db.recipes.find(), 2))


# POST request to add new recipe
def test_2_add_new_recipes(self):
    r = request.post(APITest._get_url("add_recipe"),
                     obj={data.RECIPE_OBJ})
    self.assertEqual(r.status_code, 201)  # created


# GET request to return added recipe
def test_3_get_new_recipe(self):
    cookie_name = "Chocolate Kiss Powder Puff Cookies"
    r = request.get(self._get_url_withid("get_cookie", cookie_name))
    self.assertEqual(r.status_code, 204)  # no content
    self.assertDictEqual(mongo.db.recipes.find(), {data.RECIPE_OBJ})


# PUT request to update recipe
def test_4_update_existing_recipe(self):
    id: 1002
    r = request.put(self._get_url_withid("edit_recipe", id),
                    obj=APITest.NEW_RECIPE_OBJ)
    self.assertEqual(r.status_code, 204)  # no content


# GET request to return updated recipe
def test_5_get_new_recipe_after_update(self):
    cookie_name = "Chocolate Lava Chocolate Chip Cookie Cups"
    r = request.get(self._get_url_withid("get_cookie", cookie_name))
    self.assertEqual(r.status_code, 204)  # no content
    self.assertDictEqual(mongo.db.recipes.find(), APITest.NEW_RECIPE_OBJ)


# DELETE request to remove recipe
def test_6_delete_recipe(self):
    id = 1002
    r = request.delete(self._get_url_withid("delete_recipe", id))
    self.assertEqual(r.status_code, 204)  # no content


# GET request to return removed recipe
def test_7_get_recipe_after_deletion(self):
    id = 1002
    r = request.delete(self._get_url_withid("delete_recipe", id))
    self.assertNotEqual(r.status_code, 404)  # not found
    self.assertDictNotEqual(mongo.db.recipes.find(), APITest.NEW_RECIPE_OBJ)

# verify class disabled for previous button when currentpage = 1
# verify class disabled for next button when currentpage = numberOfPages
# verify class active pageNumber when currentpage = pageNumber
# verify result of clicking previous button displays currentpage -1
# verify result of clicking next button displays currentpage +1
# verify result displayed when random pageNumber clicked
# verify numberOfPages = math.ceil(resultsCount/recipesPerPage)
# verify number of items displayed <= recipesPerPage


if __name__ == '__main__':
    unittest.main()
