import strawberry

from . import models, serializers


@strawberry.experimental.pydantic.type(
    model=serializers.UserDates,
    all_fields=True
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
    dates: Dates


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


@strawberry.input
class UserPageMeta:
    page: int = 0
    size: int = 0


@strawberry.experimental.pydantic.input(
    model=serializers.UserUpdate
)
class UserFilterMeta:
    name: str | None
    surname: str | None


@strawberry.experimental.pydantic.type(
    model=serializers.UserPaginationPage
)
class Pagination:
    size: int
    page: int


@strawberry.experimental.pydantic.type(
    model=serializers.UserFilter
)
class Filter:
    name: str | None
    surname: str | None


@strawberry.experimental.pydantic.type(
    model=serializers.UserResponse
)
class ListResponse:
    data: list[User]
    pagination: Pagination | None
    filters: Filter | None