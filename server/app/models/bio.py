from pydantic import BaseModel, HttpUrl


class SocialUrl(BaseModel):
    social_id: int
    social_name: str
    social_url: HttpUrl


class Bio(BaseModel):
    name: str
    bio: str
    social_urls: list[SocialUrl]
