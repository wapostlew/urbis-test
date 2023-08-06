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
    id: int = Field(alias="_id")
    dates: UserDates

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PydanticObjectId: str}


class UserPaginationPage(BaseModel):
    page: int = 0
    size: int = 0


class UserFilter(BaseModel):
    name: str | None = None
    surname: str | None = None


class UserResponse(BaseModel):
    data: list[UserRetrieve]
    pagination: UserPaginationPage
    filters: UserFilter