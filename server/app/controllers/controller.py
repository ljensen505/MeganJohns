from app.models.albums import Album, Artist
from app.models.artwork import Artwork, Medium
from app.queries.albums import AlbumsQueries
from app.queries.artwork import ArtworkQueries


class Controller:
    def __init__(self) -> None:
        self.album_queries = AlbumsQueries()
        self.artwork_queries = ArtworkQueries()

    def _pad_year(self, release_year) -> str:
        release_year = str(release_year)
        while len(release_year) < 4:
            release_year += "0"
        return release_year

    async def get_all_albums(self) -> list[Album]:
        albums: list[Album] = []
        rows = self.album_queries.get_all()
        for row in rows:
            release_year = row.get("release_year")
            if release_year:
                row["release_year"] = self._pad_year(release_year)
            row["artist"] = Artist(**row)
            albums.append(Album(**row))
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
        return artwork
