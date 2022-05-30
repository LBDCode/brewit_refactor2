from venv import create
import pytest

from src import create_app, db
from src.api.models import User
from src.api.models import Recipe

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app  


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope='function')
def add_user():
    def _add_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    return _add_user


@pytest.fixture(scope='function')
def add_recipe():
    def _add_recipe(title, original_gravity, final_gravity, abv, ibu, srm, yield_amt, directions, style):

        recipe = Recipe( 
            title = 'Kona Brewing Co. Imperial Coconut Stout',
            original_gravity = '1.044 (20.0°P)',
            final_gravity = '1.006 (4.2°P)',
            abv = '8%', 
            ibu ='24',
            srm = '342',
            yield_amt = '5 US gal',
            directions = 'Mash grains 90 min at 152°F (67°C). Boil 95 min, adding hops and cane sugar as indicated. Ferment at 65°F (18°C) until final gravity is reached. Rack to secondary and add toasted coconut. Allow to condition 7 days before bottling or kegging.',
            style = 'American Stout')

        db.session.add(recipe)
        db.session.commit()
        return recipe
    return _add_recipe