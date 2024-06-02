from fastapi import APIRouter

from app.controllers.controller import Controller
from app.models.artwork import Artwork

router = APIRouter(prefix="/artwork")
c = Controller()


@router.get("/")
async def all_albums() -> list[Artwork]:
    return await c.get_all_artwork()
