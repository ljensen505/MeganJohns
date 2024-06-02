from asyncio import gather
from pprint import pprint

from fastapi import FastAPI

from app.controllers.controller import Controller
from app.models.meganjohns import MeganJohns
from app.routers.albums import router as albums_router
from app.routers.artwork import router as artwork_router

app = FastAPI()
app.include_router(albums_router)
app.include_router(artwork_router)

c = Controller()

origins = ["https://localhost:3000"]


@app.get("/")
async def root() -> MeganJohns:
    # TODO: use asyncio.gather() here once more data is available
    albums = await c.get_all_albums()
    return MeganJohns(albums=albums)
