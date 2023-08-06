from fastapi import FastAPI

from app.config.db import init_db, client, db


app = FastAPI()


@app.on_event("startup")
async def start_depends():
    await init_db()