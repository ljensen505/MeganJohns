from asyncio import gather

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.controller import Controller
from app.models.meganjohns import MeganJohns
from app.routers.albums import router as albums_router
from app.routers.artwork import router as artwork_router
from app.routers.bio import router as bio_router

origins = ["http://localhost:5173"]

c = Controller()
app = FastAPI()

app.include_router(albums_router)
app.include_router(artwork_router)
app.include_router(bio_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> MeganJohns:
    albums, artwork, bio = await gather(
        c.get_all_albums(), c.get_all_artwork(), c.get_bio()
    )
    return MeganJohns(albums=albums, artwork=artwork, bio=bio)
