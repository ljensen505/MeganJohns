from fastapi import APIRouter

from app.controllers.controller import Controller
from app.models.bio import Bio

router = APIRouter(prefix="/bio")
c = Controller()


@router.get("/")
async def bio() -> Bio:
    return await c.get_bio()
