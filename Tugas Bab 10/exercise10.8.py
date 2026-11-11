# 10-8_cats_and_dogs.py
# Membaca cats.txt dan dogs.txt. Jika file tidak ada, tampilkan pesan ramah.

daftar_file = ["cats.txt", "dogs.txt"]

for nama_file in daftar_file:
    print("=" * 50)
    print(f"Isi file: {nama_file}")
    print("=" * 50)
    try:
        with open(nama_file) as file:
            isi = file.read()
    except FileNotFoundError:
        print(f"Maaf, file '{nama_file}' tidak ditemukan.")
    else:
        print(isi.rstrip())

print("\n--- Catatan ---")
print("Pindahkan salah satu file (misal dogs.txt) ke folder lain,")
print("lalu jalankan ulang untuk melihat blok except bekerja.")