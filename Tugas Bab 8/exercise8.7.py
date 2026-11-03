def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

album_1 = make_album("Pink Floyd", "The Dark Side of the Moon")
album_2 = make_album("Queen", "A Night at the Opera")
album_3 = make_album("Coldplay", "Parachutes", songs=10)

print(album_1)
print(album_2)
print(album_3)