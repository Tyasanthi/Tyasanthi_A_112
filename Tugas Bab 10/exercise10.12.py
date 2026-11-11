# Jika angka favorit sudah tersimpan, tampilkan; jika belum, tanya dan simpan.
import json
import os

FOLDER_SCRIPT = os.path.dirname(os.path.abspath(__file__))
NAMA_FILE_JSON = os.path.join(FOLDER_SCRIPT, "favorite_number.json")

try:
    with open(NAMA_FILE_JSON) as file:
        angka = json.load(file)
except FileNotFoundError:
    angka = input("Masukkan angka favorit Anda: ")
    with open(NAMA_FILE_JSON, "w") as file:
        json.dump(angka, file)
        print(f"Angka favorit Anda disimpan di:\n  {NAMA_FILE_JSON}")
else:
    print(f"Selamat datang kembali! Saya tahu angka favorit Anda yaitu {angka}.")