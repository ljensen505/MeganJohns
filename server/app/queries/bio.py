from pprint import pprint

from app.queries.base import BaseQueries


class BioQueries(BaseQueries):
    def __init__(self) -> None:
        super().__init__()

    def get_all_social(self) -> list[dict]:
        cursor, conn = self.get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT * FROM {self.social_table}
            """
        )
        rows: list[dict] = cursor.fetchall()  # type: ignore
        self.close_cursor_and_conn(cursor, conn)
        return rows

    def get_all_bio_content(self) -> dict:
        cursor, conn = self.get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT * FROM {self.bio_content_table}
            WHERE id = 1;
            """  # hardcoded because only one bio in table
        )
        row: dict = cursor.fetchone()  # type: ignore
        self.close_cursor_and_conn(cursor, conn)
        return row
