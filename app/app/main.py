import strawberry
from faker import Faker
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

from app.config.db import init_db, client, db
from app.apps import user

app = FastAPI()


@app.on_event("startup")
async def start_depends():
    await init_db()
    fake = Faker()
    for _ in range(10):
        Faker.seed()
        await user.models.User(
            **user.serializers.UserCreate(
                name=fake.first_name(), surname=fake.last_name()
            ).dict()
        ).create()

graphql_app = GraphQLRouter(
    strawberry.Schema(
        query=user.queries.Query,
        mutation=user.mutations.Mutation,
    )
)
app.include_router(graphql_app, prefix="/grapthql")