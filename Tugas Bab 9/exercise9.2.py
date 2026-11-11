# uji_tiga_restoran.py
# Uji coba tiga instance Restaurant untuk latihan 9-2.

from restaurant import Restaurant

resto1 = Restaurant("Sate Pak Kumis", "Sate")
resto2 = Restaurant("Pizza Hut", "Italia")
resto3 = Restaurant("Sushi Tei", "Jepang")

for resto in (resto1, resto2, resto3):
    resto.describe_restaurant()
    print("-" * 30)