from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from starlette.status import HTTP_204_NO_CONTENT

from api.schemas.joke import Joke
from api.schemas.joke_type import JokeType
from api.services.joke import Joke as Service


router = APIRouter()


@router.get('/jokes/random', response_model=Joke, tags=["Jokes"])
async def random(param: JokeType):
    service = Service()
    return service.get(param)


@router.get('/jokes', response_model=list[Joke], tags=["Jokes"])
async def index():
    pass


@router.get('/jokes/{id}', response_model=Joke, tags=["Jokes"])
async def show(id: int):
    pass


@router.post('/jokes', response_model=Joke, tags=["Jokes"])
async def store(joke: Joke):
    pass


@router.put('/jokes/{id}', response_model=Joke, tags=["Jokes"])
async def update(id: int, joke: Joke):
    pass


@router.delete("/jokes/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Jokes"])
async def destroy(id: int):
    return Response(status_code=HTTP_204_NO_CONTENT)

