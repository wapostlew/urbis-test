import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

from app.config.db import init_db, client, db
from app.apps import user

app = FastAPI()


@app.on_event("startup")
async def start_depends():
    await init_db()

graphql_app = GraphQLRouter(
    strawberry.Schema(
        query=user.queries.Query,
        mutation=user.mutations.Mutation,
    )
)
app.include_router(graphql_app, prefix="/grapthql")