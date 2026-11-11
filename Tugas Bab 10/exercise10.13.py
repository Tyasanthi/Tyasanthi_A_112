# Menyimpan info pengguna dalam dictionary ke JSON,
# Tambahan agar tersimpan di folder Tugas bab 10

import json
import os

# Bangun path JSON relatif terhadap lokasi file .py
FOLDER_SCRIPT   = os.path.dirname(os.path.abspath(__file__))
NAMA_FILE_JSON  = os.path.join(FOLDER_SCRIPT, "user_info.json")

# --- Kumpulkan beberapa informasi ---
info_user = {
    "username"     : input("Masukkan username    : "),
    "nama_lengkap" : input("Masukkan nama lengkap: "),
    "kota"         : input("Masukkan kota asal   : "),
    "hobi"         : input("Masukkan hobi        : "),
}

# --- Simpan ke file JSON ---
with open(NAMA_FILE_JSON, "w") as file:
    json.dump(info_user, file, indent=4)

print(f"\nInformasi disimpan di:\n  {NAMA_FILE_JSON}")

# --- Baca kembali untuk verifikasi ---
print("\nMembaca kembali dari file...")
print("=" * 45)

with open(NAMA_FILE_JSON) as file:
    data = json.load(file)

print("Ringkasan yang program ingat:")
for kunci, nilai in data.items():
    print(f"  {kunci:12}: {nilai}")