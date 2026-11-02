gunung = ["Bromo", "Rinjani", "Krakatau", "Jayawijaya", "Kilimanjaro"]

# ======================================
# 1. Membuat IndexError dengan sengaja
# ======================================
#print("Mencoba mengakses indeks 5 (padahal list hanya punya indeks 0-4): ")
#print(gunung[5])   #IndexError: list index out of range

# Indeks yang valid: 0, 1, 2, 3, 4  (atau -1, -2, -3, -4, -5)
print("Mengakses indeks 4 (elemen terakhir):")
print(gunung[4])          #Kilimanjaro

print("\nMengakses indeks -1 (cara aman untuk elemen terakhir):")
print(gunung[-1])         #Kilimanjaro

print("\nJumlah elemen:", len(gunung))