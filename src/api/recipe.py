from flask import Blueprint, request
from flask_restx import Resource, Api, fields

from src import db
from src.api.models import Recipe


recipe_blueprint = Blueprint('recipe', __name__)
api = Api(recipe_blueprint)

recipe = api.model('Recipe', {
    'recipe_id': fields.Integer(readOnly=True), 
    'title': fields.String(required=True), 
    'original_gravity':  fields.String(required=True), 
    'final_gravity': fields.String(required=True), 
    'abv': fields.String(required=True),  
    'ibu': fields.String(required=True),  
    'srm': fields.String(required=True), 
    'yield_amt': fields.String(required=True), 
    'directions': fields.String(required=True), 
    'style': fields.String(required=True)

})


class Recipes(Resource):

    @api.marshal_with(recipe)
    def get(self, recipe_id):
        recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
        if not recipe:
            api.abort(404, f"Recipe {recipe_id} does not exist")
            return recipe, 200


class RecipesList(Resource):

    @api.marshal_with(recipe, as_list=True)
    def get(self):
        return Recipe.query.all(), 200




        
api.add_resource(Recipes, '/recipe/<int:recipe_id>')
api.add_resource(RecipesList, '/recipe')
