import strawberry

from . import models, serializers


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


@strawberry.experimental.pydantic.input(
    model=serializers.UserPaginationPage
)
class UserPaginationPage:
    page: int
    size: int


@strawberry.experimental.pydantic.input(
    model=serializers.UserUpdate
)
class UserFilterMeta:
    name: str | None
    surname: str | None