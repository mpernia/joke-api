from decouple import config
from api.models import joke_sql


def create_tables():
    if config('DB_CONNECTION') == 'mongodb':
        pass
    else:
        joke_sql.create_jokes_table()