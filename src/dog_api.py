import requests


class Dog_api:
    def __init__(self):
        self.url = 'https://dog.ceo/api/'

    def list_all_breeds(self):
        self.url = self.url + 'breeds/list/all'
        response = requests.get(self.url)
        return response

    def random_image(self):
        self.url=self.url+'breeds/image/random'
        response = requests.get(self.url)
        return response

    def image_by_breed(self, breed):
        self.url=self.url+f'breed/{breed}/images'
        response = requests.get(self.url)
        return response

    def sub_breed_by_breed(self, breed):
        self.url=self.url+f'breed/{breed}/list'
        response = requests.get(self.url)
        return response

    def random_image_by_breed(self, breed):
        self.url=self.url+f'breed/{breed}/images/random'
        response = requests.get(self.url)
        return response