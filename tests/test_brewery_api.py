from src.openbrewery import Openbrewery_api
import pytest


@pytest.mark.parametrize('city', ['new_york', 'san_diego', 'kharkov'])
def test_get_breweries_by_city(city):
    api = Openbrewery_api()
    response = api.get_breweries_by_city(city)
    assert response.status_code == 200


@pytest.mark.parametrize('state', ['ohio', 'new_york', 'texas'])
def test_get_breweries_by_state(state):
    api = Openbrewery_api()
    response = api.get_breweries_by_state(state)
    assert response.status_code == 200


@pytest.mark.parametrize('brewery', ['madtree-brewing-cincinnati', 'barn-brewery-san-diego',
                                     'ballast-point-brewing-company-little-italy-san-diego'])
def test_get_brewery(brewery):
    api = Openbrewery_api()
    response = api.get_brewery(brewery)
    assert response.status_code == 200


@pytest.mark.parametrize('query', ['dog', 'cat', 'bird'])
def test_get_breweries_search_by_query(query):
    api = Openbrewery_api()
    response = api.get_breweries_search_by_query(query)
    assert response.status_code == 200


@pytest.mark.parametrize('query', ['dog', 'cat', 'bird'])
def test_get_breweries_autocomplete_by_query(query):
    api = Openbrewery_api()
    response = api.get_breweries_autocomplete_by_query(query)
    assert response.status_code == 200
