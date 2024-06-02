from typing import Optional

from pydantic import BaseModel, HttpUrl


class Medium(BaseModel):
    medium_id: int
    medium_name: str


class Artwork(BaseModel):
    artwork_id: int
    artwork_name: str
    medium: Medium
    source_url: HttpUrl
    release_year: str
    size: Optional[str] = None
