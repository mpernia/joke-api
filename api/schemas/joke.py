from datetime import datetime
from pydantic import BaseModel


class Joke(BaseModel):
    id: int = None
    uuid: str = None
    text: str = None
    type: str = None
    created_at: datetime = None
    updated_at: datetime = None
    deleted_at: datetime = None
