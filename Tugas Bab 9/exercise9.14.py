import random

# Pool: 10 angka dan 5 huruf
pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]

# Memilih 4 elemen unik secara acak
pemenang = random.sample(pool, 4)

print(f"Pool            : {pool}")
print(f"Kombinasi menang: {pemenang}")
print("Tiket yang cocok dengan 4 angka/huruf ini memenangkan hadiah!")