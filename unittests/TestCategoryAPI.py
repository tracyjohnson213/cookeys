import unittest
import os
from flask import Flask, request
from flask_pymongo import PyMongo
import unittests.recipedata as data

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")
mongo = PyMongo(app)


class Test_CategoryAPI(unittest.TestCase):
    API_URL = "https://8080-e6fbbb44-6582-4788-b88f-5b9232d23bb0.ws-us02.gitpod.io/"


# variable for new url with route
def _get_url(self, route):
    return "{}/{}".format(Test_CategoryAPI.API_URL, route)


# variable for new url with route and any item;
# replacing whitespace in str(item)
def _get_url_withid(self, route, item):
    return "{}/{}/{}".format(Test_CategoryAPI.API_URL,
                             route, item.replace("", "%20"))


# --- CATEGORIES TESTs
# GET request to return all categories
def test_1_get_all_categories(self):
    r = request.get(self._get_url('/get_categories'))
    self.assertEqual(r.status_code, 200)  # ok
    self.assertEqual(len(mongo.db.categories.find(), 2))


# POST request to add new category
def test_2_add_new_categor(self):
    r = request.post(Test_CategoryAPI._get_url('/add_category'),
                     obj=data.CATEGORY_OBJ)
    self.assertEqual(r.status_code, 201)  # created


# GET request to return added category
def test_3_get_new_category(self):
    id = data.CATEGORY_OBJ._id
    r = request.get(self._get_url_withid('/edit_category', id))
    self.assertEqual(r.status_code, 200)  # ok
    self.assertDictEqual(mongo.db.categories.find(),
                         data.CATEGORY_OBJ)


# POST request to add new recipe with added category
"""def test_2_add_new_recipes_with_new_category(self):"""


# GET request to return added recipe with added category
"""def test_3_get_new_recipe_with_new_category(self):"""


# PUT request to update category
def test_4_update_existing_category(self):
    id = data.CATEGORY_OBJ._id
    r = request.put(self._get_url_withid('/edit_category', id),
                    obj=Test_CategoryAPI.NEW_CATEGORY_OBJ)
    self.assertEqual(r.status_code, 204)  # no content


# GET request to return updated category
def test_5_get_new_category_after_update(self):
    id = data.CATEGORY_OBJ._id
    r = request.get(self._get_url_withid('/edit_category', id))
    self.assertEqual(r.status_code, 204)  # no content
    self.assertDictEqual(mongo.db.categories.find(),
                         Test_CategoryAPI.NEW_CATEGORY_OBJ)


# GET request to return recipe with updated category
"""def test_3_get_recipe_with_updated_category(self):"""


# DELETE request to remove category
def test_6_delete_category(self):
    id = data.CATEGORY_OBJ._id
    r = request.delete(self._get_url_withid("/delete_category", id))
    self.assertEqual(r.status_code, 204)  # no content


# GET request to return removed category
def test_7_get_category_after_deletion(self):
    id = data.CATEGORY_OBJ._id
    r = request.get(self._get_url_withid('/edit_category', id))
    self.assertEqual(r.status_code, 404)  # not found
    self.assertDictNotEqual(mongo.db.categories.find(),
                            Test_CategoryAPI.NEW_CATEGORY_OBJ)


# GET request to return recipe without deleted category
"""def test_3_get_recipe_without_deleted_category(self):"""


if __name__ == '__main__':
    unittest.main()
