import json

def test_recpie(test_app):
    client = test_app.test_client()
    response = client.get('/recipe')
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'Maui' in data['title']
    assert data['recipe_id'] == 2327