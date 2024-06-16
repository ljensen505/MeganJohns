from fastapi import APIRouter

from app.controllers.controller import Controller
from app.models.quotes import Quote

router = APIRouter(prefix="/quotes")
c = Controller()


@router.get("")
async def all_quotes() -> list[Quote]:
    return await c.get_all_quotes()
