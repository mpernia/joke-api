from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session
from api.config.database import INIT_DB
from api.schemas.joke import Joke
from api.schemas.new_joke import NewJoke
from api.schemas.edit_joke import EditJoke
from api.schemas.joke_type import JokeType
from api.services.joke import Joke as JokeService
from api.repositories.joke import Repository as JokeRepository


router = APIRouter()


@router.get('/jokes/random', response_model=Joke, tags=["Jokes"])
async def random(param: JokeType, db: Session = INIT_DB):
    joke_service = JokeService()
    return JokeRepository.store(joke_service.get(param), db)


@router.get('/jokes', response_model=list[Joke], tags=["Jokes"])
async def index(start: int = 1, limit: int = 10, db: Session = INIT_DB):
    return JokeRepository.all(start, limit, db)


@router.get('/jokes/{id}', response_model=Joke, tags=["Jokes"])
async def show(id: int, db: Session = INIT_DB):
    return JokeRepository.find(id, db)


@router.post('/jokes', response_model=Joke, tags=["Jokes"])
async def store(joke: NewJoke, db: Session = INIT_DB):
    return JokeRepository.store(joke, db)


@router.put('/jokes/{id}', response_model=Joke, tags=["Jokes"])
async def update(id: int, joke: EditJoke, db: Session = INIT_DB):
    return JokeRepository.update(id, joke, db)


@router.delete("/jokes/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Jokes"])
async def destroy(id: int, db: Session = INIT_DB):
    JokeRepository.delete(id, db)
    return Response(status_code=HTTP_204_NO_CONTENT)

