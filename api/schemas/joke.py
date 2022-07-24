from datetime import datetime
from pydantic import BaseModel
from api.schemas.joke_type import JokeType


class Joke(BaseModel):
    id: int
    text: str
    type: JokeType
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
