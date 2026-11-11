# eksplorasi_random.py
# Eksplorasi modul 'random' (Python Module of the Week) untuk latihan 9-16.

import random

print("Eksplorasi Modul 'random'")
print("=" * 40)

# random.choice - pilih satu item
print("choice        :", random.choice(["apel", "jeruk", "mangga"]))

# random.sample - pilih beberapa unik
print("sample        :", random.sample(range(1, 50), 6))

# random.shuffle - acak urutan
kartu = list(range(1, 11))
random.shuffle(kartu)
print("shuffle       :", kartu)

# random.uniform - float dalam rentang
print("uniform       :", round(random.uniform(1.0, 10.0), 2))

# random.seed - hasil bisa direproduksi
random.seed(42)
print("seed=42       :", [random.randint(1, 6) for _ in range(5)])