import strawberry, datetime
from . import serializers, models, otypes, inputs


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_user(self, data: inputs.UserCreate) -> otypes.User:
        data = await models.User(name=data.name, surname=data.surname).create()
        return serializers.UserRetrieve(**data.dict())

    @strawberry.mutation
    async def update_user(self, _id:int, data: inputs.UserUpdate) -> otypes.User:
        user = await models.User.get(_id)
        await user.update({
            "$set": data.to_pydantic().dict(exclude_none=True)
        })
        return serializers.UserRetrieve(**user.dict())

    @strawberry.field
    async def auth_user(self, _id: int) -> otypes.User:
        user = await models.User.get(_id)
        data = await user.update({
            "$set": {
                "dates.lastlogin": datetime.datetime.now(),
                # "dates.register_date": datetime.datetime.now() - datetime.timedelta(days=2)
            }
        })
        print(user.dict())
        print(serializers.UserRetrieve(**data.dict()))
        return serializers.UserRetrieve(**data.dict())