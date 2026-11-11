# Meminta angka favorit pengguna dan menyimpannya dengan json.dumps().
import json
import os

# Folder tempat file .py ini berada
FOLDER_SCRIPT = os.path.dirname(os.path.abspath(__file__))
NAMA_FILE_JSON = os.path.join(FOLDER_SCRIPT, "favorite_number.json")

angka = input("Masukkan angka favorit Anda: ")

with open(NAMA_FILE_JSON, "w") as file:
    json.dump(angka, file)

print(f"Angka favorit Anda disimpan di:\n  {NAMA_FILE_JSON}")