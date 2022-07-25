from decouple import config
from api.models.joke_sql import JokeSql
from api.models.joke_mongo import JokeMongo


Model = (JokeSql, JokeMongo)[config("DB_CONNECTION") == 'mongodb']

