import datetime
import itertools

from beanie import Document
from pydantic import BaseModel, Field


user_id = itertools.count(1)

class UserDates(BaseModel):
    lastlogin_date: datetime.datetime | None = Field(alias="lastlogin")
    register_date: datetime.datetime = Field(default_factory=datetime.datetime.now, alias="register")


class User(Document):
    id: int = Field(default_factory=lambda: next(user_id))
    name: str
    surname: str
    dates: UserDates = UserDates()

    class Settings:
        name = "user"