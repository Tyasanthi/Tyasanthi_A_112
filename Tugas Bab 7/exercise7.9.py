sandwich_orders = ["tuna", "pastrami", "ham", "pastrami", "veggie",
                   "pastrami", "turkey", "club"]
finished_sandwiches = []

print("Maaf, deli sudah kehabisan pastrami!")

# Hapus SEMUA pastrami dari daftar pesanan
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(f"Pesanan yang diproses: {sandwich_orders}\n")

# Buat sandwich yang tersisa
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Saya membuat sandwich {sandwich} Anda.")
    finished_sandwiches.append(sandwich)

print("\nSemua sandwich sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"  - {sandwich}")