# 10-4_guest.py
# Meminta nama pengguna lalu menyimpannya ke guest.txt.

nama = input("Silakan masukkan nama Anda: ")

with open("guest.txt", "w") as file:
    file.write(nama)

print(f"Nama '{nama}' telah disimpan ke guest.txt.")