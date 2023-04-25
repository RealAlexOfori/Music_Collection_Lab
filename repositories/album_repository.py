from db.run_sql import run_sql

from models.album import Album #  ADDED
from models.artist import Artist
import repositories.artist_repository as artist_repo

def select_all():  
    albums = []  # ADDED - in case we get `None` back from run_sql

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repo.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'] )
        albums.append(album)
    return albums

def save(album):
    sql = f"INSERT INTO albums (title, genre, artist_id) VALUES (%s,%s,%s) RETURNING *"
    values = [album.title,  album.genre, album.artist.id]
    rows = run_sql(sql, values)
    id = rows[0]['id']
    album.id = id 
    return album

def select(id):
    task = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]

    rows = run_sql(sql, values)
    #could also have len(rows) > 0
    if rows:
        album_info = rows[0]
        artist = artist_repo.select(album_info['artist_id'])
        album = Album(album_info['title'],  album_info['genre'], artist, album_info['id'])

    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (title,  genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]

    run_sql(sql, values)