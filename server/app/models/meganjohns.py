from pydantic import BaseModel

from app.models.albums import Album
from app.models.artwork import Artwork
from app.models.bio import Bio


class MeganJohns(BaseModel):
    albums: list[Album]
    artwork: list[Artwork]
    bio: Bio
