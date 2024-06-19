from pathlib import Path

from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from app.constants import (
    ALBUMS_TABLE,
    ART_MEDIUM_TABLE,
    ARTICLES_TABLE,
    ARTISTS_TABLE,
    ARTWORK_TABLE,
    BIO_CONTENT_TABLE,
    QUOTES_TABLE,
    SOCIAL_TABLE,
    VIDEOS_TABLE,
)
from app.db.conn import connect_db
from app.models.albums import Album, Artist
from app.models.articles import Article
from app.models.artwork import Artwork, Medium
from app.models.bio import Bio, SocialUrl
from app.models.quotes import Quote
from app.models.video import Video

# videos
videos = [
    Video(
        id=0,
        title="Human",
        subtitle="Official Music Video",
        description="Song and Video Written, Performed, Produced, Recorded, Filmed and Edited by Megan Johns.",
        youtube_player="""<iframe width="560" height="315" src="https://www.youtube.com/embed/HiskLzZHX48?si=yomwnyr4FkupXU1e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
    ),
    Video(
        id=0,
        title="Feathers",
        subtitle="Dark Fantasy Drama",
        description="Written and Directed by Megan Johns. Featuring Sara Blythe. With Malakhai Schnell, Dylan Fix-Carter, Aaron Nelson, Robin Nelson, Breann Pleasant, Andre Royal Sr., Shannon Swords, Zoe Wassman, Sofia Dumitru and Tracy Ilene Miller. Walter King - Director of Photography",
        youtube_player="""<iframe width="560" height="315" src="https://www.youtube.com/embed/tk8LlaAwgCg?si=olWVWRrhVEVxhFKp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
    ),
]

# quotes
quotes = [
    Quote(
        id=0,
        body="Something like Trent Reznor taking over the Smashing Pumpkins and replacing Corgan with Tori Amos.",
        author="Middle Tennessee Music",
        source="https://www.indiemusicdiscovery.com/megan-johns-says-hey-lonely/",  # type: ignore
    ),
    Quote(
        id=0,
        body="Melodic and hypnotizing. | Best Local Singer-Songwriter 2013",
        author="Smile Politely",
        source="http://www.smilepolitely.com/music/best_music_2013/",  # type: ignore
    ),
    Quote(
        id=0,
        body="Tight aggressive power chords underpin Johns's raspy yet melodic singing voice, telling a story in impressionistic fragments rather than a single narrative.",
        author="Eugene Magazine",
    ),
    Quote(
        id=0,
        body="Johns creates music that is at once sweet and biting: the languid tone of her voice providing a perfect lace overlay to the harder-rocking arrangements beneath them.",
        author="The News Gazette",
    ),
    Quote(
        id=0,
        body="She lures her listeners to unearth a deeper subconscious level.",
        author="The Buzz Weekly",
    ),
]

# art mediums
arcylic = Medium(id=0, medium_name="Acrylic on Canvas")
oil = Medium(id=0, medium_name="Oil on Canvas")
zinc = Medium(id=0, medium_name="Zinc Plate Etching")
charcol = Medium(id=0, medium_name="Charcol on Paper")
rice_paper = Medium(id=0, medium_name="Pen and Ink on Rice Paper")
watercolor = Medium(id=0, medium_name="Watercolor on Paper En Plein Air")
illustrator_poster = Medium(id=0, medium_name="Illustrator Poster")

mediums = [arcylic, oil, zinc, charcol, rice_paper, watercolor, illustrator_poster]

# Social & Bio information
socials = [
    SocialUrl(
        id=0,
        social_name="itunes",
        social_url="https://itunes.apple.com/us/artist/megan-johns/74351585",  # type: ignore
    ),
    SocialUrl(
        id=0,
        social_name="facebook",
        social_url="http://www.facebook.com/meganjohnsmusic",  # type: ignore
    ),
    SocialUrl(
        id=0,
        social_name="soundcloud",
        social_url="https://soundcloud.com/meganjohns",  # type: ignore
    ),
    SocialUrl(
        id=0,
        social_name="youtube",
        social_url="http://youtube.com/user/MeganJohnsVideos",  # type: ignore
    ),
    SocialUrl(
        id=0,
        social_name="instagram",
        social_url="https://instagram.com/meganjohnsmusic/",  # type: ignore
    ),
    SocialUrl(
        id=0,
        social_name="spotify",
        social_url="https://open.spotify.com/artist/3CTUWD06ndDSuuUUJHm1bf",  # type: ignore
    ),
]

bio_html_content = ""

ROOT_DIR = Path(__file__).parent
HTML_FILE = ROOT_DIR / "bio.html"
with open(HTML_FILE, "r") as html_file:
    for line in html_file.readlines():
        bio_html_content += line.strip()

bio = Bio(name="Megan Johns", bio=bio_html_content, social_urls=socials)

# artwork
# TODO: image urls here are not necessary high-quality and may change
# TODO: this list is not complete
artwork: list[Artwork] = [
    Artwork(
        id=0,
        artwork_name="Women's March",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349704/MeganJohns/women-s-march-2017-megan-johns-acrylic-on-canvas-2018_kayuo0.jpg",  # type: ignore
        release_year="2017",
        size='24"x36"',
    ),
    Artwork(
        id=0,
        artwork_name="Teatime Study",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349801/MeganJohns/megan-johns-teapot-and-cup-study_orig_w7fpkp.jpg",  # type: ignore
        release_year="2017",
        size='11"x24"',
    ),
    Artwork(
        id=0,
        artwork_name="Spilled Beans Study",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349883/MeganJohns/megan-johns-spill-the-beans-study_tedajt.jpg",  # type: ignore
        release_year="2017",
        size='12"x12"',
    ),
    Artwork(
        id=0,
        artwork_name="Silver Teapot Study",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349883/MeganJohns/silver-teapot-study-megan-johns-acrylic-on-canvas-2018_l7jiuu.jpg",  # type: ignore
        release_year="2017",
        size='12"x12"',
    ),
    Artwork(
        id=0,
        artwork_name="Captain",
        medium=zinc,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349882/MeganJohns/megan-johns-22captain-22-zinc-plate-etching_orig_jr9krw.jpg",  # type: ignore
        release_year="2009",
        size='9"x12"',
    ),
    Artwork(
        id=0,
        artwork_name="Gas Mask Study",
        medium=oil,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349882/MeganJohns/gas-mask-study_vxcdny.jpg",  # type: ignore
        release_year="2009",
        size='11"x14"',
    ),
    Artwork(
        id=0,
        artwork_name="Portrait of Kathleen (In Progress)",
        medium=arcylic,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349882/MeganJohns/portrait-of-kathleen-megan-johns_pw4bj2.jpg",  # type: ignore
        release_year="2018",
        size='16"x20"',
    ),
    Artwork(
        id=0,
        artwork_name="Domestic Mystery",
        medium=oil,
        source_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717349882/MeganJohns/megan-johns-22untitled-22-oil-on-canvas_orig_f5botg.jpg",  # type: ignore
        release_year="2009",
        size='06"x20"',
    ),
    Artwork(
        id=0,
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
    id=0,
    artist_name="Megan Johns",
    artist_url="https://music.apple.com/us/artist/megan-johns/74351585",  # type: ignore
)
greytones = Artist(
    id=0,
    artist_name="The Greytones",
    artist_url="https://open.spotify.com/artist/5JyA3JrRMinqhLslj7EyLl",  # type: ignore
)
bubble_bubble_bum_bum = Artist(
    id=0,
    artist_name="Bubble Bubble Gum Gum",
    artist_url="https://music.apple.com/us/artist/bubble-bubble-gum-gum/1554007615",  # type: ignore
)
artists: list[Artist] = [megan_artist, greytones, bubble_bubble_bum_bum]

# discography
albums: list[Album] = [
    Album(
        id=0,
        album_name="Dirty Shoes",
        release_year="2005",
        artist=megan_artist,
        apple_music_url="https://music.apple.com/us/album/dirty-shoes/74351635",  # type: ignore
        bandcamp_url="https://meganjohns.bandcamp.com/track/fog",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363942/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Dirty_Shoes_Cover_2005_bnb8u0.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/track=2275072448/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/track/fog">Fog by Megan Johns</a></iframe>',
    ),
    Album(
        id=0,
        album_name="Hey, Lonely",
        release_year="2012",
        artist=megan_artist,
        apple_music_url="https://music.apple.com/us/album/hey-lonely/565637660",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363966/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Hey_Lonely_Jacket_hires-2_kwo34f.jpg",  # type: ignore
        rear_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717364028/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Hey_Lonely_Reverse2_esmjia.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=2623205502/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/album/hey-lonely">Hey, Lonely by Megan Johns</a></iframe>',
    ),
    Album(
        id=0,
        album_name="Gemini",
        release_year="2015",
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/track/gemini",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363956/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Gemini_MoonWish_Single_2015_spgv2m.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/track=2493215358/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/track/gemini">Gemini by Moonwish</a></iframe>',
    ),
    Album(
        id=0,
        album_name="Inner Voice",
        release_year="2019",
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/album/inner-voice-ep",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363981/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Inner_Voice_EP_2019_po0nbq.jpg",  # type: ignore
        rear_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363984/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Inner_Voice_EP_Backcover_2019_ilenfq.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=1645073059/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/album/inner-voice-ep">Inner Voice EP by Megan Johns</a></iframe>',
    ),
    Album(
        id=0,
        album_name="MoonWish Recordings 2015",
        release_year="2015",
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/album/moonwish-recordings-2015",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363988/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/MoonWish_Recordings_2015_j3pzyd.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=3211709152/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/album/moonwish-recordings-2015">MoonWish Recordings 2015 by Megan Johns</a></iframe>',
    ),
    Album(
        id=0,
        album_name="Penumbra",
        release_year="2007",
        artist=greytones,
        spotify_url="https://open.spotify.com/album/1FMhRBPjhCOe21JNwgYUAb",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363997/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/The_Greytones_Penumbra_Cover_2007_rh02wu.jpg",  # type: ignore
    ),
    Album(
        id=0,
        album_name="Feathers",
        release_year="2021",
        artist=bubble_bubble_bum_bum,
        spotify_url="https://music.apple.com/us/album/feathers-original-motion-picture-score/1554024529",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363949/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Feathers_Score_Bubble_Bubble_Gum_Gum_2021_itjio0.jpg",  # type: ignore
    ),
    Album(
        id=0,
        album_name="Human",
        release_year="2022",
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/track/human",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363973/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/Human_Single_2022_lknlpc.png",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/track=3620590740/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/track/human">Human by Megan Johns</a></iframe>',
    ),
    Album(
        id=0,
        album_name="I Am Old",
        release_year="2022",
        artist=megan_artist,
        bandcamp_url="https://meganjohns.bandcamp.com/track/i-am-old",  # type: ignore
        front_artwork_url="https://res.cloudinary.com/dreftv0ue/image/upload/v1717363976/MeganJohns/Discography%20-%20Album%20%2B%20Single%20Covers/I_Am_Old_Single_2022_mao2yw.jpg",  # type: ignore
        bandcamp_player='<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/track=2078638263/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://meganjohns.bandcamp.com/track/i-am-old">I Am Old by Megan Johns</a></iframe>',
    ),
]


def get_db_cursor() -> tuple[MySQLConnection, MySQLCursor]:
    db = connect_db()
    cursor = db.cursor()
    return db, cursor


def close_db_cursor(db: MySQLConnection, cursor: MySQLCursor) -> None:
    db.commit()
    cursor.close()
    db.close()


def drop_tables():
    db, cursor = get_db_cursor()
    for table in [
        ALBUMS_TABLE,
        ARTISTS_TABLE,
        ARTICLES_TABLE,
        ARTWORK_TABLE,
        ART_MEDIUM_TABLE,
        BIO_CONTENT_TABLE,
        SOCIAL_TABLE,
        QUOTES_TABLE,
        VIDEOS_TABLE,
    ]:
        print(f"dropping table: {table}")
        cursor.execute(
            f"""-- sql
        DROP TABLE IF EXISTS {table};
        """
        )
    close_db_cursor(db, cursor)
    print("")


def seed_albums() -> None:
    print(f"seeding {len(albums)} albums")
    db, cursor = get_db_cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {ALBUMS_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            album_name VARCHAR(255) NOT NULL,
            release_year YEAR,
            artist_id INT NOT NULL,
            spotify_url VARCHAR(255),
            itunes_url VARCHAR(255),
            bandcamp_url VARCHAR(255),
            apple_music_url VARCHAR(255),
            front_artwork_url VARCHAR(255),
            rear_artwork_url VARCHAR(255),
            bandcamp_player VARCHAR(1024),
            PRIMARY KEY (id),
            FOREIGN KEY (artist_id) REFERENCES {ARTISTS_TABLE}(id) ON DELETE CASCADE
        );
        """
    )
    for album in albums:
        cursor.execute(
            f"""-- sql
            INSERT INTO {ALBUMS_TABLE} (album_name, release_year, artist_id, spotify_url, itunes_url, bandcamp_url, apple_music_url, front_artwork_url, rear_artwork_url, bandcamp_player)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                album.album_name,
                album.release_year,
                album.artist.id,
                str(album.spotify_url) if album.spotify_url else None,
                str(album.itunes_url) if album.itunes_url else None,
                str(album.bandcamp_url) if album.bandcamp_url else None,
                str(album.apple_music_url) if album.apple_music_url else None,
                str(album.front_artwork_url) if album.front_artwork_url else None,
                str(album.rear_artwork_url) if album.rear_artwork_url else None,
                album.bandcamp_player,
            ),
        )
        if cursor.lastrowid:
            album.id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()


def seed_quotes() -> None:
    print(f"seeding {len(quotes)} quotes")
    db, cursor = get_db_cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {QUOTES_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            body VARCHAR(1000) NOT NULL,
            author VARCHAR(255) NOT NULL,
            source VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
    )
    for quote in quotes:
        cursor.execute(
            f"""-- sql
            INSERT INTO {QUOTES_TABLE} (body, author, source)
            VALUES (%s, %s, %s);
            """,
            (quote.body, quote.author, str(quote.source) if quote.source else None),
        )
        if cursor.lastrowid:
            quote.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_artists() -> None:
    print(f"seeding {len(artists)} artists")
    db, cursor = get_db_cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {ARTISTS_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            artist_name VARCHAR(255) NOT NULL,
            artist_url VARCHAR(255) NOT NULL,
            PRIMARY KEY (id)
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
            artist.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_articles():
    print(f"seeding {len(articles)} articles")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE articles (
            id INT NOT NULL AUTO_INCREMENT,
            article_title VARCHAR(255) NOT NULL,
            body VARCHAR(255) NOT NULL,
            video_url VARCHAR(255),
            is_featured BOOLEAN DEFAULT FALSE,
            PRIMARY KEY (id)
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
            article.id = cursor.lastrowid

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
            id INT NOT NULL AUTO_INCREMENT,
            medium_id INT NOT NULL,
            artwork_name VARCHAR(255) UNIQUE NOT NULL,
            source_url VARCHAR(255) NOT NULL,
            release_year YEAR NOT NULL,
            size VARCHAR(255),
            PRIMARY KEY (id),
            FOREIGN KEY (medium_id) REFERENCES {ART_MEDIUM_TABLE}(id) ON DELETE CASCADE
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
                work.medium.id,
                work.artwork_name,
                str(work.source_url) if work.source_url else None,
                work.release_year,
                work.size,
            ),
        )
        if cursor.lastrowid:
            work.id = cursor.lastrowid

    close_db_cursor(db, cursor)


def seed_art_mediums():
    print(f"seeding {len(mediums)} art mediums")
    db, cursor = get_db_cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {ART_MEDIUM_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            medium_name VARCHAR(255),
            PRIMARY KEY (id)
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
            medium.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_social_info():
    print(f"seeding {len(socials)} social urls")
    db, cursor = get_db_cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {SOCIAL_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            social_name VARCHAR(255) NOT NULL UNIQUE,
            social_url VARCHAR(255) NOT NULL UNIQUE,
            primary key (id)
        );
        """
    )
    for s in socials:
        cursor.execute(
            f"""-- sql
            INSERT INTO {SOCIAL_TABLE} (social_name, social_url)
            VALUES (%s, %s);
            """,
            (s.social_name, str(s.social_url)),
        )
        if cursor.lastrowid:
            s.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def seed_bio():
    print(f"seeding single bio")
    db, cursor = get_db_cursor()

    cursor.execute(
        f"""-- sql
        CREATE TABLE {BIO_CONTENT_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            content TEXT NOT NULL,
            primary key (id)
        );
        """
    )
    cursor.execute(
        f"""-- sql
        INSERT INTO {BIO_CONTENT_TABLE} (content)
        VALUES (%s);
        """,
        (bio.bio,),
    )
    close_db_cursor(db, cursor)


def seed_videos() -> None:
    print(f"seeding single bio")
    db, cursor = get_db_cursor()
    cursor.execute(
        f"""-- sql
        CREATE TABLE {VIDEOS_TABLE} (
            id INT NOT NULL AUTO_INCREMENT,
            title VARCHAR(255) NOT NULL,
            subtitle VARCHAR(255) NOT NULL,
            description VARCHAR(1000) NOT NULL,
            youtube_player VARCHAR(5000),
            primary key (id)
        );
        """
    )
    for video in videos:
        cursor.execute(
            f"""-- sql
            INSERT INTO {VIDEOS_TABLE} (title, subtitle, description, youtube_player)
            VALUES (%s, %s, %s, %s);
            """,
            (video.title, video.subtitle, video.description, video.youtube_player),
        )
        if cursor.lastrowid:
            video.id = cursor.lastrowid
    close_db_cursor(db, cursor)


def main() -> None:
    drop_tables()
    seed_artists()
    seed_albums()
    seed_articles()
    seed_art_mediums()
    seed_artwork()
    seed_social_info()
    seed_bio()
    seed_quotes()
    seed_videos()
