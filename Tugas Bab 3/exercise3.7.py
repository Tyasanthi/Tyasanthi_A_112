tamu = ["Kaya", "Djilva", "Vrysa", "Desy"]
for teman in tamu:
    print(f"Hai {teman}, ayo makan malam di rumahku.")

print("\nAyo ajak yang lain juga!\n")

tamu.insert(0, "Ganisa")
tamu.insert(2, "Adena")
tamu.append("Windi")

for teman in tamu:
    print(f"Hai {teman}, ayo makan malam di rumahku.")

print("\nSayangnya saat ini aku kekurangan meja, jadi aku hanya bisa mengajak 2 orang saja.\n")

while len(tamu) > 2:
    tamu_batal = tamu.pop()
    print(f"Maaf {tamu_batal}, aku tidak jadi mengajak kamu makan malam.")

print()
for teman in tamu:
    print(f"{teman}, kamu masih diundang makan malam!")

del tamu[0]
del tamu[0]

print(f"List tamu fix: {tamu}")