from pprint import pprint

from app.queries.base import BaseQueries


class AlbumsQueries(BaseQueries):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self) -> list[dict]:
        cursor, conn = self.get_cursor_and_conn()
        # TODO: this will need a join
        cursor.execute(
            f"""-- sql
            SELECT * FROM {self.albums_table}
            INNER JOIN {self.artists_table}
            ON {self.albums_table}.artist_id = {self.artists_table}.artist_id
            """
        )
        data: list[dict] = cursor.fetchall()  # type: ignore
        self.close_cursor_and_conn(cursor, conn)
        return data
