from datetime import datetime
from pydantic import BaseModel


class EditJoke(BaseModel):
    text: str = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
