import sqlite3

CREATE_ARTIST_TABLE = """CREATE TABLE IF NOT EXISTS artists (
    artist_id INTEGER PRIMARY KEY UNIQUE,
    artist_name TEXT NOT NULL UNIQUE
    );"""

CREATE_ALBUM_TABLE = """CREATE TABLE IF NOT EXISTS albums (
    album_id INTEGER PRIMARY KEY UNIQUE,
    album_name TEXT NOT NULL UNIQUE,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists
    );"""

INSERT_ARTIST = "INSERT INTO artists (artist_name) VALUES (?);"
SELECT_ALL_ARTISTS = "SELECT * FROM artists ORDER BY artist_name ASC;"
INSERT_ALBUM = "INSERT INTO albums (album_name, artist_id) VALUES (?,?);"
SELECT_ALL_ALBUMS = "SELECT album_id, album_name FROM albums INNER JOIN artists ON artists.artist_id = albums.artist_id;"


connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_ARTIST_TABLE)
        connection.execute(CREATE_ALBUM_TABLE)


def add_artist(artist_name):
    try:
        with connection:
            connection.execute(INSERT_ARTIST, (artist_name,))
    except:
        print("error")


def add_album(album_name, artist_id):
    with connection:
        connection.execute(INSERT_ALBUM, (album_name, artist_id,))


def get_artsits():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_ARTISTS)
        return cursor.fetchall()


def get_albums():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_ALBUMS)
        return cursor.fetchall()
