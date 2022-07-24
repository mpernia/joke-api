import requests
import json


class Joke:
    HTTP_HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    URL_CHUCK = 'https://api.chucknorris.io/jokes/random'
    URL_DAD = 'https://icanhazdadjoke.com/'

    @staticmethod
    def get_chuck_joke(self, payload = None):
        response = requests.request("GET", self.URL_CHUCK, headers=self.HTTP_HEADERS, data=payload).text
        return json.loads(response).get('value')

    @staticmethod
    def get_dad_joke(self, payload: dict = None):
        response = requests.request("GET", self.URL_DAD, headers=self.HTTP_HEADERS, data=payload).text
        return json.loads(response).get('joke')

    def get(self, type: str, payload: dict = None):
        if type == "chuck":
            joke = self.get_chuck_joke(self, payload)
        else:
            joke = self.get_dad_joke(self, payload)

        return joke

