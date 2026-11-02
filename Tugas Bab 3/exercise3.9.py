tamu = ["Kaya", "Djilva", "Vrysa", "Desy"]
for teman in tamu:
    print(f"Hai {teman}, ayo makan malam di rumahku.")

print("\nAyo ajak yang lain juga!\n")

tamu.insert(0, "Ganisa")
tamu.insert(2, "Adena")
tamu.append("Windi")

for teman in tamu:
    print(f"Hai {teman}, ayo makan malam di rumahku.")

#3.9, hitung jumlah tamu dengan len()
print(f"\nAku mengajak {len(tamu)} orang untuk makan malam.")