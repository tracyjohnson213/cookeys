from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'myCookeys'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/myCookeys'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_all_recipes():
    recipe = mongo.db.recipes
    output = []
    for r in recipe.find():
        output.append({'cookie_name' : r['cookie_name'], 'image_source' : r['image_source']})
    return jsonify({'result' : output})