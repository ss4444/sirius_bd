from fastapi import FastAPI
from app.core.db import database
from app.api.routes import router


app = FastAPI()


app.state.database = database


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


app.include_router(router=router)
