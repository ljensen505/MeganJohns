from typing import Optional

from pydantic import BaseModel, HttpUrl


class Artist(BaseModel):
    artist_id: int
    artist_name: str
    artist_url: Optional[HttpUrl] = None


class Album(BaseModel):
    album_id: int
    album_name: str
    release_year: str
    artist: Artist
    spotify_url: Optional[HttpUrl] = None
    itunes_url: Optional[HttpUrl] = None
    bandcamp_url: Optional[HttpUrl] = None
    apple_music_url: Optional[HttpUrl] = None
