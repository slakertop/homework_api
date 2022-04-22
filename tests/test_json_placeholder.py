from src.jsonplaceholder import JSONplaceholder_api
import pytest


@pytest.mark.parametrize('title', ['заголовок', 'ЗАГОЛОВОК', 'ЗаГоЛоВоК'])
def test_post_posts(title):
    api = JSONplaceholder_api()
    response = api.post_posts(title, 'тело', '55')
    assert response.status_code == 201
    assert response.json()['title'] == title


def test_get_posts():
    api = JSONplaceholder_api()
    response = api.get_posts()
    assert response.status_code == 200


@pytest.mark.parametrize('id', [1, 2, 3])
def test_get_post(id):
    api = JSONplaceholder_api()
    response = api.get_post(id)
    assert response.status_code == 200
    assert response.json()['id'] == id


@pytest.mark.parametrize('id', [1, 2, 3])
def test_get_post_comments(id):
    api = JSONplaceholder_api()
    response = api.get_post_comments(id)
    assert response.status_code == 200
    assert response.json()[0]['postId'] == id


@pytest.mark.parametrize('id', [1, 2, 3])
def test_put_post(id):
    api = JSONplaceholder_api()
    response = api.put_post(id, title='заголовок', body='тело', userId=666)
    assert response.status_code == 200
    assert response.json()['id'] == id
