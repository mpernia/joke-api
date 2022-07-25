from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from api.schemas.joke import Joke
from api.schemas.new_joke import NewJoke
from api.schemas.edit_joke import EditJoke
from api.models.joke import Model


class Repository():
    @staticmethod
    def all(start: int, limit: int, session: Session):
        return session.query(
            Model.id,
            Model.uuid,
            Model.text,
            Model.type,
            Model.created_at,
            Model.updated_at
        ).filter(Model.id >= start).limit(limit).all()

    @staticmethod
    def store(joke: NewJoke, session: Session):
        db_joke = Model(
            uuid=joke.uuid,
            text=joke.text,
            type=joke.type,
            created_at=joke.created_at,
            updated_at=joke.updated_at
        )
        session.add(db_joke)
        session.commit()
        session.refresh(db_joke)
        return db_joke

    @staticmethod
    def update(id: int, joke: EditJoke, session: Session):
        db_joke = Repository.find(id, session)
        db_joke.text = joke.text
        db_joke.updated_at = datetime.now()
        db_joke.deleted_at = None
        session.commit()
        session.refresh(db_joke)
        return db_joke

    @staticmethod
    def delete(id: int, session: Session):
        db_joke = Repository.find(id, session)
        session.query(Model).filter(Model.id == id).delete()
        session.commit()
        return {'message' : f'successfully deleted joke with id: {id}'}

    @staticmethod
    def find(id: int, session: Session):
        db_joke = session.query(Model).filter(Model.id == id).first()
        if db_joke is None:
            raise HTTPException(status_code=404, detail='This joke does not exist')
        return db_joke

