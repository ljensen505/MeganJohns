from typing import Optional

from pydantic import BaseModel, HttpUrl


class Quote(BaseModel):
    quote_id: int
    body: str
    author: str
    source: Optional[HttpUrl] = None
