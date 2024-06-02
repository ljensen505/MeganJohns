from app.queries.base import BaseQueries


class ArticlesQueries(BaseQueries):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self) -> list[dict]:
        cursor, conn = self.get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT * FROM {self.articles_table}
            """
        )
        data: list[dict] = cursor.fetchall()  # type: ignore
        self.close_cursor_and_conn(cursor, conn)
        return data
