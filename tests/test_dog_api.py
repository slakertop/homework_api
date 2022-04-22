from src.dog_api import Dog_api
import pytest


def test_dog_api_all_breeds():
    api = Dog_api()
    response = api.list_all_breeds()
    assert response.status_code == 200


def test_dog_api_random_image():
    api = Dog_api()
    response = api.random_image()
    assert response.status_code == 200


@pytest.mark.parametrize('breed', ['akita', 'boxer', 'chow', 'dingo'])
def test_dog_api_image_by_breed(breed):
    api = Dog_api()
    response = api.image_by_breed(breed)
    assert response.status_code == 200


@pytest.mark.parametrize('breed', ['akita', 'boxer', 'chow', 'dingo'])
def test_dog_api_sub_breed_by_breed(breed):
    api = Dog_api()
    response = api.sub_breed_by_breed(breed)
    assert response.status_code == 200


@pytest.mark.parametrize('breed', ['akita', 'boxer', 'chow', 'dingo'])
def test_dog_api_random_image_by_breed(breed):
    api = Dog_api()
    response = api.random_image_by_breed(breed)
    assert response.status_code == 200
