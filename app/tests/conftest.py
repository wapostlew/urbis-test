import os

import pytest

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from httpx import AsyncClient

from app.config.db import init_db
from app.settings import document_models
from app.main import app


async def mock_database():
    client: AsyncIOMotorClient = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    db: AsyncIOMotorDatabase = client['urbis-test']
    await init_beanie(
        database=db,
        recreate_views=True,
        document_models=document_models
    )


@pytest.fixture
async def client_test(mocker):
    mocker.patch("app.config.db.init_db", return_value=await mock_database())

    async with AsyncClient(
        app=app, base_url="http://localhost:8000", follow_redirects=True
    ) as ac:
        yield ac


@pytest.fixture
def anyio_backend():
    return "asyncio"