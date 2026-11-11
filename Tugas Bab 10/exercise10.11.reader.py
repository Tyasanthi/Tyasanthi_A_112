# Membaca angka favorit dari file JSON dan menampilkan pesan.
# 10-11_favorite_number_reader.py — versi aman
import json
import os

FOLDER_SCRIPT = os.path.dirname(os.path.abspath(__file__))
NAMA_FILE_JSON = os.path.join(FOLDER_SCRIPT, "favorite_number.json")

with open(NAMA_FILE_JSON) as file:
    angka = json.load(file)

print(f"Saya tahu angka favorit Anda! Yaitu {angka}.")