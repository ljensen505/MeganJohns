from pprint import pprint

from app.queries.base import BaseQueries


class AlbumsQueries(BaseQueries):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self) -> list[dict]:
        cursor, conn = self.get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT
                	al.id,
                    al.album_name ,
                    al.release_year,
                    al.artist_id ,
                    al.spotify_url ,
                    al.itunes_url ,
                    al.bandcamp_url ,
                    al.apple_music_url ,
                    al.front_artwork_url ,
                    al.rear_artwork_url ,
                    al.bandcamp_player ,
                    ar.artist_name ,
                    ar.artist_url
            FROM {self.albums_table} al
            INNER JOIN {self.artists_table} ar
            ON al.artist_id = ar.id
            """
        )
        data: list[dict] = cursor.fetchall()  # type: ignore
        self.close_cursor_and_conn(cursor, conn)
        return data
