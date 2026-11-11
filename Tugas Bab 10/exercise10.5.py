# 10-5_guest_book.py
# Loop meminta nama pengguna dan menyimpannya ke guest_book.txt
# (satu nama per baris). Ketik 'selesai' untuk keluar.

print("Buku Tamu Digital - ketik 'selesai' untuk keluar.")
print("=" * 50)

with open("guest_book.txt", "w") as file:
    while True:
        nama = input("Masukkan nama: ")
        if nama.lower() == "selesai":
            break
        if nama.strip():
            file.write(f"{nama}\n")
            print(f"  -> '{nama}' telah dicatat.")

print("\nSemua nama tersimpan di guest_book.txt.")