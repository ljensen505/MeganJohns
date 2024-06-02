from fastapi import APIRouter

from app.controllers.controller import Controller
from app.models.albums import Album

router = APIRouter(prefix="/albums")
c = Controller()


@router.get("/")
async def all_albums() -> list[Album]:
    return await c.get_all_albums()
