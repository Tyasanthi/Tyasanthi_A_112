def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print("Masukkan data album (ketik 'quit' untuk berhenti).")

while True:
    artist = input("Nama artis: ")
    if artist == "quit":
        break
    title = input("Judul album: ")
    album = make_album(artist, title)
    print(f"Album dicatat: {album}\n")