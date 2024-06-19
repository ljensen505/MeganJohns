from pprint import pprint

from app.queries.base import BaseQueries


class ArtworkQueries(BaseQueries):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self) -> list[dict]:
        cursor, conn = self.get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT 
                a.id,
                a.medium_id ,
                a.artwork_name ,
                a.source_url ,
                a.release_year ,
                a.`size` ,
                m.id as medium_id,
                m.medium_name
            FROM {self.artwork_table} a
            INNER JOIN {self.medium_table} m
            ON a.medium_id = m.id
            """
        )
        rows: list[dict] = cursor.fetchall()  # type: ignore
        self.close_cursor_and_conn(cursor, conn)
        return rows
