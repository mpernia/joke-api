import json
import requests
from datetime import datetime
from api.schemas import joke as schema
from api.schemas.joke_type import JokeType

class Joke:
    HTTP_HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    URL_CHUCK = 'https://api.chucknorris.io/jokes/random'
    URL_DAD = 'https://icanhazdadjoke.com/'

    def parse_response(self, uuid, text, type):
        now = datetime.utcnow()
        joke = schema.Joke()
        joke.uuid = uuid
        joke.text = text
        joke.type = type
        joke.created_at = now
        joke.updated_at = now
        return joke

    @staticmethod
    def get_chuck_joke(self, payload = None):
        response = requests.request("GET", self.URL_CHUCK, headers=self.HTTP_HEADERS, data=payload).text
        joke_json = json.loads(response)
        return self.parse_response(joke_json.get('id'), joke_json.get('value'), JokeType.chuck)

    @staticmethod
    def get_dad_joke(self, payload: dict = None):
        response = requests.request("GET", self.URL_DAD, headers=self.HTTP_HEADERS, data=payload).text
        joke_json = json.loads(response)
        return self.parse_response(joke_json.get('id'), joke_json.get('joke'), JokeType.dad)

    def get(self, type: str, payload: dict = None):
        if type == "chuck":
            joke = self.get_chuck_joke(self, payload)
        else:
            joke = self.get_dad_joke(self, payload)
        return joke

