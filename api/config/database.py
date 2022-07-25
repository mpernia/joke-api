from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import HTTPException, Depends

DB_CONNECTION = config("DB_CONNECTION")
DB_HOST = config("DB_HOST")
DB_USER = config("DB_USER")
DB_PASSWORD = ('', ':' + config("DB_PASSWORD"))[config("DB_PASSWORD") != '']
DB_NAME = config("DB_NAME")

Base = None


def mysql():
    return f'mysql+pymysql://{DB_USER}{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


def pgsql():
    return f'postgresql://{DB_USER}{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


def sqlite():
    return f'sqlite:///./{DB_NAME}'


def mongodb():
    return f'mongodb+srv://{DB_USER}{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true&w=majority'


def connections(name):
    drivers = {
        'mysql': mysql,
        'pgsql': pgsql,
        'sqlite': sqlite,
        'mongodb': mongodb
    }
    func = drivers.get(name, lambda: 'error')
    return func()


if connections(config('DB_CONNECTION')) == 'error':
    raise HTTPException(500, 'Invalid database driver')

DATABASE_URL = connections(config('DB_CONNECTION'))

if config('DB_CONNECTION') == 'mongodb':
    pass
else:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()


def sql_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def mongo_db():
    pass


INIT_DB = (Depends(sql_db), Depends(mongo_db))[config("DB_CONNECTION") == 'mongodb']

