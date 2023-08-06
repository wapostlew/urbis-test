import datetime
import strawberry

from beanie import PydanticObjectId

from . import models, serializers


PyObjectIdType = strawberry.scalar(
    PydanticObjectId,
    serialize=str,
    parse_value=lambda v: PyObjectIdType(v)
)

@strawberry.experimental.pydantic.type(
    model=serializers.UserDates,
    # all_fields=True
    fields=[
        "lastlogin_date",
        "register_date",
    ]
)
class Dates:
    pass


@strawberry.experimental.pydantic.type(
    model=serializers.UserRetrieve,
)
class User:

    id: int
    name: strawberry.auto
    surname: strawberry.auto
    dates: strawberry.LazyType["Dates", __name__]


@strawberry.experimental.pydantic.input(
    model=serializers.UserCreate,
)
class UserCreate:
    name: str
    surname: str

@strawberry.experimental.pydantic.input(
    model=serializers.UserUpdate,
)
class UserUpdate:
    name: str | None
    surname: str | None