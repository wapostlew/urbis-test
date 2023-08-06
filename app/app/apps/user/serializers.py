import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class UserDates(BaseModel):
    lastlogin_date: datetime.datetime | None = Field(alias="lastlogin")
    register_date: datetime.datetime = Field(alias="register")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class UserCreate(BaseModel):
    name: str
    surname: str


class UserUpdate(BaseModel):
    name: str | None
    surname: str | None


class UserRetrieve(UserCreate):
    id: PydanticObjectId = Field(alias="_id")
    dates: UserDates

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PydanticObjectId: str}