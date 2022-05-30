import json
from src.api.models import Recipe

def test_add_recipe(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/recipe', 
        data=json.dumps({
            'title': 'Maui Brewing Co. Imperial Coconut Porter',
            'original_gravity' : '1.087 (21.0°P)',
            'final_gravity' : '1.019 (4.8°P)',
            'abv' : '9%', 
            'ibu' :'25',
            'srm' : '345',
            'yield_amt' : '5 US gal',
            'directions' : 'Mash grains 60 min at 152°F (67°C). Boil 90 min, adding hops and cane sugar as indicated. Ferment at 65°F (18°C) until final gravity is reached. Rack to secondary and add toasted coconut. Allow to condition 7 days before bottling or kegging.',
            'style' : 'American Porter'
        }),
        content_type='application/json',        
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'Added recipe: Maui Brewing Co. Imperial Coconut Porter' in data['message']




def test_single_recipe(test_app, test_database, add_recipe):
    test_database.session.query(Recipe).delete()

    recipe = add_recipe('Kona Brewing Co. Imperial Coconut Stout', '1.044 (20.0°P)', '1.006 (4.2°P)', '8%', '24', '342',  '5 US gal', 'Mash grains 90 min at 152°F (67°C). Boil 95 min, adding hops and cane sugar as indicated. Ferment at 65°F (18°C) until final gravity is reached. Rack to secondary and add toasted coconut. Allow to condition 7 days before bottling or kegging.',
        'American Stout')
 
    client = test_app.test_client()
    resp = client.get(f'/recipe/{recipe.recipe_id}')
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert 'American' in data['style']
    assert 'Maui' in data['title']
 


