from restaurant import Restaurant

resto = Restaurant("Bakso Pak Tono", "Bakso")

print(f"Pelanggan dilayani (awal)  : {resto.number_served}")

resto.number_served = 25
print(f"Setelah diubah langsung    : {resto.number_served}")

resto.set_number_served(100)
print(f"Setelah set_number_served  : {resto.number_served}")

resto.increment_number_served(50)
print(f"Setelah increment_number_served: {resto.number_served}")