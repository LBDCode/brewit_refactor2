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

    @api.expect(recipe, validate=True)
    def post(self):
        post_data = request.get_json()
        title = post_data.get('title') 
        original_gravity = post_data.get('original_gravity') 
        final_gravity = post_data.get('final_gravity') 
        abv = post_data.get('abv')  
        ibu = post_data.get('ibu')  
        srm = post_data.get('srm') 
        yield_amt = post_data.get('yield_amt') 
        directions = post_data.get('directions') 
        style = post_data.get('style') 

        response_object = {}

        recipe = Recipe.query.filter_by(title=title).first()
        
        if recipe:
            response_object['message'] = 'Sorry.  That recipe already exists.'
            return response_object, 400

        db.session.add(Recipe(title=title, original_gravity=original_gravity, final_gravity=final_gravity, abv=abv, ibu=ibu, srm=srm,
            yield_amt=yield_amt, directions=directions, style=style))
        db.session.commit()

        response_object['message'] = f'Added recipe: {title}'
        return response_object, 201


    @api.marshal_with(recipe, as_list=True)
    def get(self):
        return Recipe.query.all(), 200



        
api.add_resource(Recipes, '/recipe/<int:recipe_id>')
api.add_resource(RecipesList, '/recipe')
