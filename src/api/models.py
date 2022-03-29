from sqlalchemy.sql import func

from src import db


class User(db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class Recipe(db.Model):

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    title = db.Column(db.String(128), nullable=False)
    original_gravity = db.Column(db.String(128), nullable=True) 
    final_gravity = db.Column(db.String(128), nullable=True)
    abv = db.Column(db.String(128), nullable=True) 
    ibu = db.Column(db.String(128), nullable=True) 
    srm = db.Column(db.String(128), nullable=True) 
    yield_amt = db.Column(db.String(128), nullable=True) 
    directions = db.Column(db.Text, nullable=True)
    style = db.Column(db.String(128), nullable=True)

    def __init__(self, title, original_gravity, 
        final_gravity, abv, ibu, srm, yield_amt, directions, style):
        self.title = title
        self.original_gravity = original_gravity
        self.final_gravity = final_gravity
        self.abv = abv
        self.ibu = ibu
        self.srm = srm
        self.yield_amt = yield_amt
        self.directions = directions
        self.style = style