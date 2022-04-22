import requests


class JSONplaceholder_api:
    def __init__(self):
        self.url = 'https://jsonplaceholder.typicode.com'

    def post_posts(self, title, body, userId):
        self.url = self.url + '/posts'
        response = requests.post(self.url, data={'title': title, 'body': body, 'userId': userId})
        return response

    def get_posts(self):
        self.url = self.url + '/posts'
        response = requests.get(self.url)
        return response

    def get_post(self, id):
        self.url = self.url + f'/posts/{id}'
        response = requests.get(self.url)
        return response

    def get_post_comments(self, id):
        self.url = self.url + f'/posts/{id}/comments'
        response = requests.get(self.url)
        return response

    def put_post(self, id, title, body, userId):
        self.url = self.url + f'/posts/{id}'
        response = requests.put(self.url, data={'id': id, 'title': title, 'body': body, 'userId': userId})
        return response
