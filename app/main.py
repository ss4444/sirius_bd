from fastapi import FastAPI
from app.core.db import database
from app.models import Laboratory
from app.schemas import Lab

app = FastAPI()

app.state.database = database

origins = ["*"]


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database.disconnect()


@app.get("/get_all")
async def get_all():
    return await Laboratory.objects.all()


@app.post("/create")
async def create(data: Lab):
    await Laboratory.objects.create(**data.model_dump())
    return 1
