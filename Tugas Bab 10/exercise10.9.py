# 10-9_silent_cats_dogs.py
# Sama seperti 10-8 tetapi GAGAL secara senyap (tanpa pesan error).

daftar_file = ["cats.txt", "dogs.txt"]

for nama_file in daftar_file:
    try:
        with open(nama_file) as file:
            isi = file.read()
    except FileNotFoundError:
        pass  # gagal senyap
    else:
        print("=" * 50)
        print(f"Isi file: {nama_file}")
        print("=" * 50)
        print(isi.rstrip())
        print()

print("Program selesai (file yang tidak ada dilewati tanpa pesan).")