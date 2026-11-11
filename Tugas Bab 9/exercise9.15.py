import random

# Pool: 10 angka dan 5 huruf
pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]

# Tiket saya (pilih acak 4 elemen)
my_ticket = random.sample(pool, 4)
print(f"Tiket saya: {my_ticket}")

percobaan = 0
while True:
    percobaan += 1
    hasil = random.sample(pool, 4)
    if set(hasil) == set(my_ticket):
        break

print(f"Tiket menang setelah {percobaan:,} kali percobaan.")
print(f"Hasil undian: {hasil}")