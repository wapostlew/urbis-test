import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class UserDates(BaseModel):
    lastlogin_date: datetime.datetime | None = Field(default=None, serialization_alias="lastlogin")
    register_date: datetime.datetime = Field(default_factory=datetime.datetime.now, serialization_alias="register")


class UserCreate(BaseModel):
    name: str
    surname: str


class UserUpdate(BaseModel):
    name: str | None = None
    surname: str | None = None


class UserRetrieve(UserCreate):
    id: PydanticObjectId = Field(serialization_alias="_id")
    dates: UserDates