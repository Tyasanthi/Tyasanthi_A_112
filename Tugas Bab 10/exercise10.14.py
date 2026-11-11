# konfirmasi apakah user saat ini sama dengan user terakhir yang login.
# JSON tersimpan di folder yang sama dengan file .py ini.

import json
import os

FOLDER_SCRIPT  = os.path.dirname(os.path.abspath(__file__))
NAMA_FILE_JSON = os.path.join(FOLDER_SCRIPT, "user_login.json")


def dapatkan_username():
    """Minta username baru dari pengguna."""
    return input("Masukkan username Anda: ")


def dapatkan_username_baru():
    """Minta username baru karena user sebelumnya bukan Anda."""
    print("Baik, mari buat username baru.")
    username = input("Masukkan username baru: ")
    with open(NAMA_FILE_JSON, "w") as file:
        json.dump(username, file)
    print(f"Username disimpan di:\n  {NAMA_FILE_JSON}")
    return username


def sapa_user(username):
    """Sapa pengguna."""
    print(f"Selamat datang kembali, {username}!")


def konfirmasi_user(username):
    """Tanyakan apakah username ini benar milik pengguna."""
    jawaban = input(f"Apakah Anda {username}? (y/n): ")
    return jawaban.lower().startswith("y")


# --- Alur utama ---
try:
    with open(NAMA_FILE_JSON) as file:
        username = json.load(file)
except FileNotFoundError:
    # Pertama kali dijalankan
    username = dapatkan_username()
    with open(NAMA_FILE_JSON, "w") as file:
        json.dump(username, file)
    print(f"Kami akan mengingat Anda saat kembali, {username}!")
    print(f"Username disimpan di:\n  {NAMA_FILE_JSON}")
else:
    if konfirmasi_user(username):
        sapa_user(username)
    else:
        username = dapatkan_username_baru()
        print(f"Kami akan mengingat Anda saat kembali, {username}!")