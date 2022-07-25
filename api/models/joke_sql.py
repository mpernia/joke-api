from sqlalchemy import Column, String, Integer, DateTime
from api.config import database


class JokeSql(database.Base):
    __tablename__ = "jokes"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(80), unique=True, index=True)
    text = Column(String(255), unique=True, index=True)
    type = Column(String(10))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


def create_jokes_table():
    database.Base.metadata.create_all(database.engine)

