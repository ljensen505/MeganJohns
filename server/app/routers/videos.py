from fastapi import APIRouter

from app.controllers.controller import Controller
from app.models.video import Video

router = APIRouter(prefix="/videos")
c = Controller()


@router.get("/")
async def all_videos() -> list[Video]:
    return await c.get_all_videos()
