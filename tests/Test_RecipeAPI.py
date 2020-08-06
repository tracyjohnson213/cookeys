import unittest
import os
from flask import Flask, request
from flask_pymongo import PyMongo
import recipedata


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")
mongo = PyMongo(app)


class Test_RecipeAPI(unittest.TestCase):
    API_URL = "https://5000-bec35a3f-2a73-4d52-9097-2c12048237a7.ws-us02.gitpod.io/"

    # variable for new url with route
    def _get_url(self, route):
        return "{}/{}".format(Test_RecipeAPI.API_URL, route)


    # variable for new url with route and any item;
    # replacing whitespace in str(item)
    def _get_url_withid(self, route, item):
        return "{}/{}/{}".format(Test_RecipeAPI.API_URL,
                                route, item.replace("", "%20"))


    # --- RECIPE TESTS
    # GET request to return all recipes
    def test_1_get_all_recipes(self):
        r = request.get(Test_RecipeAPI.API_URL)
        self.assertEqual(r.status_code, 200)  # ok
        # self.assertEqual(len(mongo.db.recipes.find(), 2))


    # POST request to add new recipe
    def test_2_add_new_recipes(self):
        r = request.post(self._get_url("add_recipe"),
                        obj={recipedata.RECIPE_OBJ})
        self.assertEqual(r.status_code, 201)  # created


    # GET request to return added recipe
    def test_3_get_new_recipe(self):
        cookie_name = recipedata.RECIPE_OBJ["cookie_name"]
        r = request.get(self._get_url_withid("get_cookie", cookie_name),
                        obj=recipedata.NEW_RECIPE_OBJ)
        self.assertEqual(r.status_code, 204)  # no content
        self.assertDictEqual(mongo.db.recipes.find(), {recipedata.RECIPE_OBJ})


    # GET request to return category with added recipe
    """def test_3_get_category_with_recipe(self):"""


    # PUT request to update recipe
    def test_4_update_existing_recipe(self):
        id = recipedata.NEW_RECIPE_OBJ["_id"]
        r = request.put(self._get_url_withid("edit_recipe", id),
                        obj=recipedata.NEW_RECIPE_OBJ)
        self.assertEqual(r.status_code, 204)  # no content


    # GET request to return updated recipe
    def test_5_get_new_recipe_after_update(self):
        cookie_name = recipedata.NEW_RECIPE_OBJ["cookie_name"]
        r = request.get(self._get_url_withid("get_cookie", cookie_name))
        self.assertEqual(r.status_code, 204)  # no content
        self.assertDictEqual(mongo.db.recipes.find(),
                            recipedata.NEW_RECIPE_OBJ)


    # DELETE request to remove recipe
    def test_6_delete_recipe(self):
        id = recipedata.NEW_RECIPE_OBJ["_id"]
        r = request.delete(self._get_url_withid("delete_recipe", id))
        self.assertEqual(r.status_code, 204)  # no content


    # GET request to return removed recipe
    def test_7_get_recipe_after_deletion(self):
        id = recipedata.NEW_RECIPE_OBJ["_id"]
        r = request.delete(self._get_url_withid("delete_recipe", id))
        self.assertNotEqual(r.status_code, 404)  # not found
        # self.assertDictNotEqual(mongo.db.recipes.find(),
        #                        recipedata.NEW_RECIPE_OBJ)


if __name__ == '__main__':
    unittest.main()
