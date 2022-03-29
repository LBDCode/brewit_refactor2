import sys

from flask.cli import FlaskGroup

from src import create_app, db
from src.api.models import User, Recipe


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(User(username='mike', email='mike@test.com'))
    db.session.add(User(username='jeff', email='jeff@test.com'))

    db.session.add(Recipe( 
    title = 'Maui Brewing Co. Imperial Coconut Porter',
    original_gravity = '1.087 (21.0°P)',
    final_gravity = '1.019 (4.8°P)',
    abv = '9%', 
    ibu ='25',
    srm = '345',
    yield_amt = '5 US gal',
    directions = 'Mash grains 60 min at 152°F (67°C). Boil 90 min, adding hops and cane sugar as indicated. Ferment at 65°F (18°C) until final gravity is reached. Rack to secondary and add toasted coconut. Allow to condition 7 days before bottling or kegging.',
    style = 'American Porter')
    )

    db.session.add(Recipe( 
    title = 'Kona Brewing Co. Imperial Coconut Stout',
    original_gravity = '1.044 (20.0°P)',
    final_gravity = '1.006 (4.2°P)',
    abv = '8%', 
    ibu ='24',
    srm = '342',
    yield_amt = '5 US gal',
    directions = 'Mash grains 90 min at 152°F (67°C). Boil 95 min, adding hops and cane sugar as indicated. Ferment at 65°F (18°C) until final gravity is reached. Rack to secondary and add toasted coconut. Allow to condition 7 days before bottling or kegging.',
    style = 'American Stout'))
    db.session.commit()

if __name__ == '__main__':
    cli()