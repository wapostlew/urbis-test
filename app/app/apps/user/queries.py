import datetime

import strawberry

from . import serializers, models, otypes

@strawberry.type
class Query:

    @strawberry.field
    async def get_user(self, _id: int) -> otypes.User:
        data = await models.User.find_one({"_id": _id})
        serialize_data = serializers.UserRetrieve(**data.dict())
        return serialize_data

    @strawberry.field
    async def get_users(self) -> list[otypes.User]:
        data = await models.User.find_all().to_list()
        serialize_data = [
            serializers.UserRetrieve(**item.dict())
            for item in data
        ]
        return serialize_data

    @strawberry.field
    async def delete_user(self, _id: int) -> str:
        data = await models.User.get(_id)
        await data.delete()
        return "User deleted."