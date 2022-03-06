import os
import sys

from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

api = Api(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db = SQLAlchemy(app)

class Recipe(db.Model):
    __tablename__='recipes'
    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=True)
    original_gravity = db.Column(db.Text, nullable=True)
    final_gravity = db.Column(db.Text, nullable=True)
    abv = db.Column(db.Text, nullable=True)
    ibu = db.Column(db.Text, nullable=True)
    srm = db.Column(db.Text, nullable=True)
    batch_yield = db.Column(db.Text, nullable=True)
    directions = db.Column(db.Text, nullable=True)
    style = db.Column(db.Text, nullable=True)

    def __init__(self, recipe_id, title, original_gravity, abv, 
    ibu, srm, batch_yield, directions, style):
        self.recipe_id = recipe_id
        self.title = title
        self.original_gravity = original_gravity
        self.abv = abv
        self.ibu = ibu
        self.srm = srm
        self.batch_yield = batch_yield
        self.directions = directions
        self.style = style
        




class RecipePing(Resource):
    def get(self):
        return {
            'recipe_id': 2327, 
            'title': "Maui Brewing Co. Imperial Coconut Porter", 
            'original_gravity':  "1.087 (21.0°P)", 
            'final_gravity': "1.019 (4.8°P)", 
            'abv': "9%", 
            'ibu': "25" , 
            'srm': "345", 
            'yield': "5 US gal", 
            'directions': "Mash grains 60 min at 152°F (67°C). Boil 90 min, adding hops and cane sugar as indicated. Ferment at 65°F (18°C) until final gravity is reached. Rack to secondary and add toasted coconut. Allow to condition 7 days before bottling or kegging.",
            'style': "American Porter"
        }


api.add_resource(RecipePing, '/recipe')