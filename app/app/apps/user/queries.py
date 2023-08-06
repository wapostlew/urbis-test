import datetime

import strawberry

from . import serializers, models, otypes, inputs


@strawberry.type
class Query:

    @strawberry.field
    async def get_user(self, _id: int) -> otypes.User:
        data = await models.User.find_one({"_id": _id})
        serialize_data = serializers.UserRetrieve(**data.dict())
        return serialize_data

    @strawberry.field
    async def get_users(
            self,
            filters: inputs.UserFilterMeta | None = serializers.UserFilter(),
            pagination: inputs.UserPaginationPage | None = serializers.UserPaginationPage()
    ) -> otypes.ListResponse:
        data = await models.User.find_many(
            {
                str(k):v
                for k,v in filters.to_pydantic().dict(exclude_none=True).items()
            },
            skip=(pagination.page - 1) * pagination.size,
            limit=pagination.size
        ).to_list()

        serialize_data = [
            serializers.UserRetrieve(**item.dict())
            for item in data
        ]

        return serializers.UserResponse(
            data=serialize_data,
            pagination=pagination.to_pydantic(),
            filters=filters.to_pydantic()
        )

    @strawberry.field
    async def delete_user(self, _id: int) -> str:
        data = await models.User.get(_id)
        await data.delete()
        return "User deleted."