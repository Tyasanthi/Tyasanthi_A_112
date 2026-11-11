# 10-6_addition.py
# Menjumlahkan dua angka dengan penanganan ValueError.

print("Program Penjumlahan Dua Angka")
print("=" * 50)

try:
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua   : "))
except ValueError:
    print("Maaf, Anda harus memasukkan ANGKA, bukan teks.")
else:
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")