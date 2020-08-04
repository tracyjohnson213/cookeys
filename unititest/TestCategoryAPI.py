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


# --- CATEGORIES TESTs
# GET request to return all categories
def test_1_get_all_categories(self):
    r = request.get(self._get_url('/get_categories'))
    self.assertEqual(r.status_code, 200)  # ok
    self.assertEqual(len(mongo.db.categories.find(), 2))


# POST request to add new category
def test_2_add_new_categor(self):
    r = request.post(APITest._get_url('/add_category'),
                     obj=APITest.CATEGORY_OBJ)
    self.assertEqual(r.status_code, 201)  # created


# GET request to return added category
def test_3_get_new_category(self):
    id = 402
    r = request.get(self._get_url_withid('/edit_category', id))
    self.assertEqual(r.status_code, 200)  # ok
    self.assertDictEqual(mongo.db.categories.find(), APITest.CATEGORY_OBJ)


# PUT request to update category
def test_4_update_existing_category(self):
    id = 402
    r = request.put(self._get_url_withid('/edit_category', id),
                    obj=APITest.NEW_CATEGORY_OBJ)
    self.assertEqual(r.status_code, 204)  # no content


# GET request to return updated category
def test_5_get_new_category_after_update(self):
    id = 402
    r = request.get(self._get_url_withid('/edit_category', id))
    self.assertEqual(r.status_code, 204)  # no content
    self.assertDictEqual(mongo.db.categories.find(), APITest.NEW_CATEGORY_OBJ)


# DELETE request to remove category
def test_6_delete_category(self):
    id = 402
    r = request.delete(self._get_url_withid("/delete_category", id))
    self.assertEqual(r.status_code, 204)  # no content


# GET request to return removed category
def test_7_get_category_after_deletion(self):
    id = 402
    r = request.get(self._get_url_withid('/edit_category', id))
    self.assertEqual(r.status_code, 404)  # not found
    self.assertDictNotEqual(mongo.db.categories.find(),
                            APITest.NEW_CATEGORY_OBJ)


if __name__ == '__main__':
    unittest.main()
