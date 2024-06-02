from pydantic import BaseModel, HttpUrl
from typing import Optional

class Article(BaseModel):
    article_id: int
    article_title: str
    body: str
    is_featured: Optional[bool] = False
    video_url: Optional[HttpUrl] = None
    