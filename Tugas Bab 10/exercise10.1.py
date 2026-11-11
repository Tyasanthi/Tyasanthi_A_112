nama_file = 'learning_python.txt'

# --- Cara 1: Baca seluruh isi file sekaligus ---
print("=" * 50)
print("CARA 1: Membaca seluruh isi file")
print("=" * 50)
with open(nama_file) as file:
    isi = file.read()
    print(isi)

# --- Cara 2: Simpan baris ke list lalu loop ---
print("=" * 50)
print("CARA 2: Membaca baris per baris ke dalam list")
print("=" * 50)
with open(nama_file) as file:
    daftar_baris = file.readlines()

for baris in daftar_baris:
    print(baris.rstrip())