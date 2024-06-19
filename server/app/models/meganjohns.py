from pydantic import BaseModel

from app.models.albums import Album
from app.models.artwork import Artwork
from app.models.bio import Bio
from app.models.quotes import Quote
from app.models.video import Video


class MeganJohns(BaseModel):
    albums: list[Album]
    artwork: list[Artwork]
    quotes: list[Quote]
    videos: list[Video]
    bio: Bio
