from app.constants import (
    ALBUMS_TABLE,
    ART_MEDIUM_TABLE,
    ARTICLES_TABLE,
    ARTISTS_TABLE,
    ARTWORK_TABLE,
)
from app.db.conn import connect_db
from app.models.albums import Album, Artist
from app.models.articles import Article
from app.models.artwork import Artwork, Medium

# art mediums
arcylic = Medium(medium_id=0, medium_name="Acrylic on Canvas")
oil = Medium(medium_id=0, medium_name="Oil on Canvas")
zinc = Medium(medium_id=0, medium_name="Zinc Plate Etching")
charcol = Medium(medium_id=0, medium_name="Charcol on Paper")
rice_paper = Medium(medium_id=0, medium_name="Pen and Ink on Rice Paper")
watercolor = Medium(medium_id=0, medium_name="Watercolor on Paper En Plein Air")
illustrator_poster = Medium(medium_id=0, medium_name="Illustrator Poster")

mediums = [arcylic, oil, zinc, charcol, rice_paper, watercolor, illustrator_poster]

# artwork
# TODO: image urls here are not necessary high-quality and may change
# TODO: this list is not complete
artwork: list[Artwork] = [
    Artwork(
        artwork_id=0,
        artwork_name="Women's March",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349704/MeganJohns/women-s-march-2017-megan-johns-acrylic-on-canvas-2018_kayuo0.jpg",  # type: ignore
        release_year="2017",
        size='24"x36"',
    ),
    Artwork(
        artwork_id=0,
        artwork_name="Teatime Study",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349801/MeganJohns/megan-johns-teapot-and-cup-study_orig_w7fpkp.jpg",  # type: ignore
        release_year="2017",
        size='11"x24"',
    ),
    Artwork(
        artwork_id=0,
        artwork_name="Spilled Beans Study",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349883/MeganJohns/megan-johns-spill-the-beans-study_tedajt.jpg",  # type: ignore
        release_year="2017",
        size='12"x12"',
    ),
    Artwork(
        artwork_id=0,
        artwork_name="Silver Teapot Study",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349883/MeganJohns/silver-teapot-study-megan-johns-acrylic-on-canvas-2018_l7jiuu.jpg",  # type: ignore
        release_year="2017",
        size='12"x12"',
    ),
    Artwork(
        artwork_id=0,
        artwork_name="Captain",
        medium=zinc,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349882/MeganJohns/megan-johns-22captain-22-zinc-plate-etching_orig_jr9krw.jpg",  # type: ignore
        release_year="2009",
        size='9"x12"',
    ),
    Artwork(
        artwork_id=0,
        artwork_name="Gas Mask Study",
        medium=oil,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349882/MeganJohns/gas-mask-study_vxcdny.jpg",  # type: ignore
        release_year="2009",
        size='11"x14"',
    ),
    Artwork(
        artwork_id=0,
        artwork_name="Portrait of Kathleen (In Progress)",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349882/MeganJohns/portrait-of-kathleen-megan-johns_pw4bj2.jpg",  # type: ignore
        release_year="2018",
        size='16"x20"',
    ),
    Artwork(
        artwork_id=0,
        artwork_name="Domestic Mystery",
        medium=oil,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349882/MeganJohns/megan-johns-22untitled-22-oil-on-canvas_orig_f5botg.jpg",  # type: ignore
        release_year="2009",
        size='06"x20"',
    ),
    Artwork(
        artwork_id=0,
        artwork_name="Lady Day",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349881/MeganJohns/lady-day-megan-johns-acrylic-on-canvas-2018_qjzpcd.jpg",  # type: ignore
        release_year="2018",
        size='16"x20"',
    ),
]

# news articles
# TODO
articles: list[Article] = []

# album artists
megan_artist = Artist(
    artist_id=0,
    artist_name="Megan Johns",
    artist_url="https://music.apple.com/us/artist/megan-johns/74351585",  # type: ignore
)
greytones = Artist(
    artist_id=0,
    artist_name="The Greytones",
    artist_url="https://open.spotify.com/artist/5JyA3JrRMinqhLslj7EyLl",  # type: ignore
)
bubble_bubble_bum_bum = Artist(
    artist_id=0,
    artist_name="Bubble Bubble Gum Gum",
    artist_url="https://music.apple.com/us/artist/bubble-bubble-gum-gum/1554007615",  # type: ignore
)
artists: list[Artist] = [megan_artist, greytones, bubble_bubble_bum_bum]

# discography
albums: list[Album] = [
    Album(
        album_id=0,
        album_name="Dirty Shoes",
        release_year="2005",
        artist=megan_artist,
        apple_music_url="https://music.apple.com/us/album/dirty-shoes/74351635",  # type: ignore
    ),
    Album(
        album_id=0,
        album_name="Hey, Lonely",
        release_year="2012",
        artist=megan_artist,
        apple_music_url="https://music.apple.com/us/album/hey-lonely/565637660",  # type: ignore
    ),
    Album(
        album_id=0,
        album_name="Gemini",
        release_year="2015",
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/track/gemini",  # type: ignore
    ),
    Album(
        album_id=0,
        album_name="Inner Voice",
        release_year="2019",
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/album/inner-voice-ep",  # type: ignore
    ),
    Album(
        album_id=0,
        album_name="MoonWish Recordings 2015",
        release_year="2015",
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/album/moonwish-recordings-2015",  # type: ignore
    ),
    Album(
        album_id=0,
        album_name="Penumbra",
        release_year="2007",
        artist=greytones,
        spotify_url="https://open.spotify.com/album/1FMhRBPjhCOe21JNwgYUAb",  # type: ignore
    ),
    Album(
        album_id=0,
        album_name="Feathers",
        release_year="2021",
        artist=bubble_bubble_bum_bum,
        spotify_url="https://music.apple.com/us/album/feathers-original-motion-picture-score/1554024529",  # type: ignore
    ),
]


def drop_tables():
    db = connect_db()
    cursor = db.cursor()
    for table in [
        ALBUMS_TABLE,
        ARTISTS_TABLE,
        ARTICLES_TABLE,
        ARTWORK_TABLE,
        ART_MEDIUM_TABLE,
    ]:
        print(f"dropping table: {table}")
        cursor.execute(
            f"""-- sql
        DROP TABLE IF EXISTS {table};
        """
        )
    db.commit()
    cursor.close()
    db.close()
    print("")


def seed_albums() -> None:
    print(f"seeding {len(albums)} albums")
    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {ALBUMS_TABLE} (
            album_id INT NOT NULL AUTO_INCREMENT,
            album_name VARCHAR(255) NOT NULL,
            release_year YEAR,
            artist_id INT NOT NULL,
            spotify_url VARCHAR(255),
            itunes_url VARCHAR(255),
            bandcamp_url VARCHAR(255),
            apple_music_url VARCHAR(255),
            PRIMARY KEY (album_id),
            FOREIGN KEY (artist_id) REFERENCES {ARTISTS_TABLE}(artist_id) ON DELETE CASCADE
        );
        """
    )
    for album in albums:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ALBUMS_TABLE} (album_name, release_year, artist_id, spotify_url, itunes_url, bandcamp_url, apple_music_url)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """,
            (
                album.album_name,
                album.release_year,
                album.artist.artist_id,
                str(album.spotify_url) if album.spotify_url else None,
                str(album.itunes_url) if album.itunes_url else None,
                str(album.bandcamp_url) if album.bandcamp_url else None,
                str(album.apple_music_url) if album.apple_music_url else None,
            ),
        )
        if cursor.lastrowid:
            album.album_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()


def seed_artists() -> None:
    print(f"seeding {len(artists)} artists")
    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {ARTISTS_TABLE} (
            artist_id INT NOT NULL AUTO_INCREMENT,
            artist_name VARCHAR(255) NOT NULL,
            artist_url VARCHAR(255) NOT NULL,
            PRIMARY KEY (artist_id)
        );
        """
    )
    for artist in artists:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ARTISTS_TABLE} (artist_name, artist_url)
            VALUES (%s, %s);
            """,
            (artist.artist_name, str(artist.artist_url)),
        )
        if cursor.lastrowid:
            artist.artist_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()


def seed_articles():
    print(f"seeding {len(articles)} articles")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE articles (
            article_id INT NOT NULL AUTO_INCREMENT,
            article_title VARCHAR(255) NOT NULL,
            body VARCHAR(255) NOT NULL,
            video_url VARCHAR(255),
            is_featured BOOLEAN DEFAULT FALSE,
            PRIMARY KEY (article_id)
        );
        """
    )
    for article in articles:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ARTICLES_TABLE} (article_title, body, video_url, is_featured)
            VALUES (%s, %s, %s, %s)
            """,
            (
                article.article_title,
                article.body,
                str(article.video_url),
                article.is_featured,
            ),
        )
        if cursor.lastrowid:
            article.article_id = cursor.lastrowid

    db.commit()
    cursor.close()
    db.close()


def seed_artwork():
    print(f"seeding {len(artwork)} pieces of art")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {ARTWORK_TABLE} (
            artwork_id INT NOT NULL AUTO_INCREMENT,
            medium_id INT NOT NULL,
            artwork_name VARCHAR(255) UNIQUE NOT NULL,
            source_url VARCHAR(255) NOT NULL,
            release_year YEAR NOT NULL,
            size VARCHAR(255),
            PRIMARY KEY (artwork_id),
            FOREIGN KEY (medium_id) REFERENCES {ART_MEDIUM_TABLE}(medium_id) ON DELETE CASCADE
        );
        """
    )
    for work in artwork:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ARTWORK_TABLE} (medium_id, artwork_name, source_url, release_year, size)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (
                work.medium.medium_id,
                work.artwork_name,
                str(work.source_url) if work.source_url else None,
                work.release_year,
                work.size,
            ),
        )
        if cursor.lastrowid:
            work.artwork_id = cursor.lastrowid

    db.commit()
    cursor.close()
    db.close()


def seed_art_mediums():
    print(f"seeding {len(mediums)} art mediums")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {ART_MEDIUM_TABLE} (
            medium_id INT NOT NULL AUTO_INCREMENT,
            medium_name VARCHAR(255),
            PRIMARY KEY (medium_id)
        );
        """
    )
    for medium in mediums:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ART_MEDIUM_TABLE} (medium_name)
            VALUES (%s);
            """,
            (medium.medium_name,),
        )
        if cursor.lastrowid:
            medium.medium_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()


def main() -> None:
    drop_tables()
    seed_artists()
    seed_albums()
    seed_articles()
    seed_art_mediums()
    seed_artwork()
