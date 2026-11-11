# 10-10_common_words.py
# Menghitung berapa kali kata 'the' muncul di file teks.
# Juga membandingkan dengan 'the ' (dengan spasi) sebagai aproksimasi lebih akurat.

import os

daftar_file = [
    "pride_and_prejudice.txt",
    "moby_dick.txt",
    "alice.txt",
]

def analisis_file(nama_file):
    try:
        with open(nama_file, encoding="utf-8") as file:
            isi = file.read()
    except FileNotFoundError:
        print(f"  [File '{nama_file}' tidak ditemukan — dilewati]")
        return
    else:
        isi_lower = isi.lower()
        jumlah_the      = isi_lower.count("the")
        jumlah_the_spasi = isi_lower.count("the ")
        print(f"  Total kata 'the'        : {jumlah_the}")
        print(f"  Total kata 'the ' (spasi): {jumlah_the_spasi}")

print("Analisis frekuensi kata 'the' di beberapa file teks")
print("=" * 55)

for f in daftar_file:
    print(f"\nFile: {f}")
    analisis_file(f)