from pydantic import BaseModel, HttpUrl


class SocialUrl(BaseModel):
    social_id: int
    social_name: str
    social_url: HttpUrl


class BioParagraph(BaseModel):
    bio_paragraph_id: int
    position: int  # 1-based index for Bio's bio array. To be used in sorting.
    bio_paragraph: str  # a single paragraph to be rendered as a <p>


class Bio(BaseModel):
    name: str
    bio: list[BioParagraph]
    social_urls: list[SocialUrl]
