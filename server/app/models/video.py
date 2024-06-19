from typing import Optional

from pydantic import BaseModel


class Video(BaseModel):
    id: int
    title: str
    subtitle: str
    description: str
    youtube_player: Optional[str] = None  # an iframe from YouTube
