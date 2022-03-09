import json
from src.api.models import User


def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users', 
        data=json.dumps({
            'username': 'libby',
            'email': 'libby.duggan_dev@gmail.co'
        }),
        content_type='application/json',        
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'Added user: libby.duggan_dev@gmail.co' in data['message']


    def test_add_user_invalid_json(test_app, test_database):
        client = test_app.test_client()
        rest = client.post(
            '/users',
            data=json.dumps({}),
            content_type='application/json',
        )
        data = json.loads(resp.data.decode())
        assert rest.status_code == 400
        assert "Input payload validation failed" in data['message']


    def test_add_user_invalid_json_keys(test_app, test_database):
        client = test_app.test_client()
        resp = client.post(
                '/users',
                data=json.dumps({"email": "john@testdriven.io"}),
                content_type='application/json',
            )
        data = json.loads(resp.data.decode())
        assert resp.status_code == 400
        assert 'Input payload validation failed' in data['message']


def test_add_user_duplicate_email(test_app, test_database):
    client = test_app.test_client()
    client.post(
        '/users',
        data=json.dumps({
            'username': 'michael',
            'email': 'michael@testdriven.io'
        }),
        content_type='application/json',
    )
    resp = client.post(
        '/users',
        data=json.dumps({
            'username': 'michael',
            'email': 'michael@testdriven.io'
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Sorry.  That email already exists.' in data['message']


def test_single_user(test_app, test_database, add_user):
    user = add_user('mike','mike@test.com')
 
    client = test_app.test_client()
    resp = client.get(f'/users/{user.id}')
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert 'mike' in data['username']
    assert 'mike@test.com' in data['email']



def test_single_user_incorrect_id(test_app, test_database):
    client = test_app.test_client()
    resp = client.get('users/888')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert 'User 888 does not exist' in data['message']



def test_all_users(test_app, test_database, add_user):
    test_database.session.query(User).delete()
    add_user('mike', 'mike@test.com')
    add_user('jeff', 'jeff@test.com')

    client = test_app.test_client()
    resp = client.get('/users')
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert len(data) == 2
    assert 'mike' in data[0]['username']
    assert 'mike@test.com' in data[0]['email']
    assert 'jeff' in data[1]['username']
    assert 'jeff@test.com' in data[1]['email']