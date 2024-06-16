from icecream import ic

from app.models.albums import Album, Artist
from app.models.artwork import Artwork, Medium
from app.models.bio import Bio, SocialUrl
from app.models.quotes import Quote
from app.queries.albums import AlbumsQueries
from app.queries.artwork import ArtworkQueries
from app.queries.bio import BioQueries
from app.queries.quotes import QuotesQueries


class Controller:
    def __init__(self) -> None:
        self.album_queries = AlbumsQueries()
        self.artwork_queries = ArtworkQueries()
        self.bio_queries = BioQueries()
        self.quote_queries = QuotesQueries()

    def _pad_year(self, release_year) -> str:
        release_year = str(release_year)
        while len(release_year) < 4:
            release_year += "0"
        return release_year

    async def get_all_quotes(self) -> list[Quote]:
        return [Quote(**q) for q in self.quote_queries.get_all()]

    async def get_bio(self) -> Bio:
        bio_content = self._get_all_bio_content()

        return Bio(
            name="Megan Johns",
            bio=bio_content,
            social_urls=self._get_all_social(),
        )

    def _get_all_social(self) -> list[SocialUrl]:
        return [SocialUrl(**row) for row in self.bio_queries.get_all_social()]

    def _get_all_bio_content(self) -> str:
        bio_row = self.bio_queries.get_all_bio_content()
        return bio_row.get("content", "")

    async def get_all_albums(self) -> list[Album]:
        albums: list[Album] = []
        rows = self.album_queries.get_all()
        for row in rows:
            release_year = row.get("release_year")
            if release_year:
                row["release_year"] = self._pad_year(release_year)
            row["artist"] = Artist(**row)
            albums.append(Album(**row))
        albums.sort(key=lambda album: album.release_year, reverse=True)
        return albums

    async def get_all_artwork(self) -> list[Artwork]:
        artwork: list[Artwork] = []
        rows = self.artwork_queries.get_all()
        for row in rows:
            release_year = row.get("release_year")
            if release_year:
                row["release_year"] = self._pad_year(release_year)
            row["medium"] = Medium(**row)
            artwork.append(Artwork(**row))
        artwork.sort(key=lambda work: work.release_year, reverse=True)
        return artwork
