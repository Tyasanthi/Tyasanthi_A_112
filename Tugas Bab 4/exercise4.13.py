# Tuple menu awal (5 makanan)
jenis_makanan = ("nasi goreng", "sate ayam", "gado-gado", "rendang", "mie ayam")

print("Menu buffet: ")
for makanan in jenis_makanan:
    print(f"{makanan}")

#(Salah)Mencoba mengubah item tuple jadi TypeError
print("\nMencoba mengubah item tuple")
try:
    jenis_makanan[0] = "mie goreng"
except TypeError as e:
    print(f"TypeError: {e}")

#(Benar)Menu diganti: tulis ulang seluruh tuple
jenis_makanan = ("mie goreng", "sate ayam", "gado-gado", "bakso", "udang keju")

print("\nMenu buffet yang baru: ")
for makanan in jenis_makanan:
    print(f"{makanan}")