from asyncio import gather

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.controller import Controller
from app.models.meganjohns import MeganJohns
from app.routers.albums import router as albums_router
from app.routers.artwork import router as artwork_router
from app.routers.bio import router as bio_router
from app.routers.quotes import router as quotes_router
from app.routers.videos import router as videos_router

from .origins import origins

c = Controller()
app = FastAPI()

app.include_router(albums_router)
app.include_router(artwork_router)
app.include_router(bio_router)
app.include_router(quotes_router)
app.include_router(videos_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> MeganJohns:
    albums, artwork, bio, quotes, videos = await gather(
        c.get_all_albums(),
        c.get_all_artwork(),
        c.get_bio(),
        c.get_all_quotes(),
        c.get_all_videos(),
    )
    return MeganJohns(
        albums=albums, artwork=artwork, quotes=quotes, videos=videos, bio=bio
    )
