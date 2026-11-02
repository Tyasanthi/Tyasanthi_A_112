mobil = "subaru"

#5 test yang menghasilkan True
print("Apakah mobil == 'subaru'? Aku prediksi True.")
print(mobil == "subaru")

print("\nApakah mobil != 'audi'? Aku prediksi True.")
print(mobil != "audi")

print("\nApakah mobil.lower() == 'SUBARU'.lower()? Aku prediksi True.")
print(mobil.lower() == "SUBARU".lower())

print("\nApakah len(mobil) > 3? Aku prediksi True.")
print(len(mobil) > 3)

print("\nApakah mobil in ['subaru', 'toyota', 'honda']? Aku prediksi True.")
print(mobil in ["subaru", "toyota", "honda"])

#5 test yang menghasilkan False
print("\nApakah mobil == 'audi'? Aku prediksi False.")
print(mobil == "audi")

print("\nApakah mobil == 'Subaru'? Aku prediksi False.")
print(mobil == "Subaru")

print("\nApakah mobil != 'subaru'? Aku prediksi False.")
print(mobil != "subaru")

print("\nApakah mobil tidak in ['subaru', 'toyota']? Aku prediksi False.")
print(mobil not in ["subaru", "toyota"])

print("\nApakah len(mobil) > 10? Aku prediksi False.")
print(len(mobil) > 10)