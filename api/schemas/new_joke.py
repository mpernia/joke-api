from datetime import datetime
from pydantic import BaseModel


class NewJoke(BaseModel):
    uuid: str = None
    text: str = None
    type: str = None
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
