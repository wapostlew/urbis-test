import datetime

from beanie import Document
from pydantic import BaseModel, Field


class UserDates(BaseModel):
    lastlogin_date: datetime.datetime | None = Field(None, serialization_alias="lastlogin")
    register_date: datetime.datetime = Field(default_factory=datetime.datetime.now, serialization_alias="register")


class User(Document):
    name: str
    surname: str
    dates: UserDates = UserDates()