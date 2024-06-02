from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from app.constants import (
    ALBUMS_TABLE,
    ART_MEDIUM_TABLE,
    ARTICLES_TABLE,
    ARTISTS_TABLE,
    ARTWORK_TABLE,
)
from app.db.conn import connect_db


class BaseQueries:
    def __init__(self) -> None:
        self.albums_table = ALBUMS_TABLE
        self.articles_table = ARTICLES_TABLE
        self.artists_table = ARTISTS_TABLE
        self.artwork_table = ARTWORK_TABLE
        self.medium_table = ART_MEDIUM_TABLE

    def get_cursor_and_conn(self) -> tuple[MySQLCursor, MySQLConnection]:
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        return cursor, conn

    def close_cursor_and_conn(self, cursor: MySQLCursor, conn: MySQLConnection) -> None:
        cursor.close()
        conn.close()
