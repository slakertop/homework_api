import requests


class Openbrewery_api:
    def __init__(self):
        self.url = 'https://api.openbrewerydb.org/breweries'

    def get_breweries_by_city(self, city):
        self.url = self.url + f'?by_city={city}'
        response = requests.get(self.url)
        return response

    def get_breweries_by_state(self, state):
        self.url = self.url + f'?by_state={state}'
        response = requests.get(self.url)
        return response

    def get_breweries_search_by_query(self, query):
        self.url = self.url + f'/search?query={query}'
        response = requests.get(self.url)
        return response

    def get_breweries_autocomplete_by_query(self, query):
        self.url = self.url + f'/autocomplete?query={query}'
        response = requests.get(self.url)
        return response

    def get_brewery(self, brewery):
        self.url = self.url + f'/{brewery}'
        response = requests.get(self.url)
        return response 
