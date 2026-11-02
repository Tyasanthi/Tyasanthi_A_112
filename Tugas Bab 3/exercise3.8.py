tempat = ["Jerman", "Inggris", "Perancis", "Jepang"]

# 1. urutan asli
print("Urutan asli: ")
print(tempat)

# 2. Urutan alfabetis dengan sorted() — list asli tidak berubah
print("\nUrutan alfabetik: ")
print(sorted(tempat))

# 3. Bukti list masih urutan asli
print("\nUrutan asli masih utuh: ")
print(tempat)

# 4. Urutan alfabetis terbalik dengan sorted(reverse=True) — list asli tidak berubah
print("\nUrutan alfabetik terbalik: ")
print(sorted(tempat, reverse=True))

# 5. Buktikan list masih urutan asli
print("\nUrutan asli masih utuh: ")
print(tempat)

# 6. reverse() — mengubah urutan list secara permanen
print("\nUrutan berubah: ")
tempat.reverse()
print(tempat)

# 7. reverse() lagi — kembali ke urutan asli
print("\nKembali ke urutan semula dengan reverse() lagi: ")
tempat.reverse()
print(tempat)

# 8. sort() — urutan alfabetis permanen
print("\nUrutan berubah dengan sort() (alphabetical): ")
tempat.sort()
print(tempat)

# 9. sort(reverse=True) — urutan alfabetis terbalik permanen
print("\nUrutan berubah dengan sort(reverse=True) (reverse-alphabetical): ")
tempat.sort(reverse=True)
print(tempat)