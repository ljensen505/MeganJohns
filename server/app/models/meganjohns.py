from pydantic import BaseModel

from app.models.albums import Album


class MeganJohns(BaseModel):
    albums: list[Album]
