from typing import Optional

from pydantic import BaseModel, HttpUrl


class Quote(BaseModel):
    id: int
    body: str
    author: str
    source: Optional[HttpUrl] = None
