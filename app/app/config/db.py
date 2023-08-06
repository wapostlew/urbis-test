import os

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from beanie import init_beanie

from app.settings import document_models

print(os.getenv("MONGODB_URI"))
client: AsyncIOMotorClient = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
db: AsyncIOMotorDatabase = client[os.getenv("MONGODB_DATABASE")]


async def init_db():
    await init_beanie(
        database=db,
        document_models=document_models,
    )