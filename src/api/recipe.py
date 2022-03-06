from flask import Blueprint
from flask_restx import Resource, Api


recipe_blueprint = Blueprint('recipe', __name__)
api = Api(recipe_blueprint)


class Recipe(Resource):
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

api.add_resource(Recipe, '/recipe')