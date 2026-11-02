# ============================================================
# 1. Tes kesamaan dan ketidaksamaan string
# ============================================================
mobil = "subaru"

print("1a. Apakah mobil == 'subaru'? Saya prediksi Benar.")
print(mobil == "subaru")

print("\n1b. Apakah mobil == 'honda'? Saya prediksi Salah.")
print(mobil == "honda")

print("\n1c. Apakah mobil != 'honda'? Saya prediksi Benar.")
print(mobil != "honda")

print("\n1d. Apakah mobil != 'subaru'? Saya prediksi Salah.")
print(mobil != "subaru")

# ============================================================
# 2. Tes menggunakan method lower()
# ============================================================
print("\n2a. Apakah mobil.lower() == 'subaru'? Saya prediksi Benar.")
print(mobil.lower() == "subaru")

print("\n2b. Apakah mobil.lower() == 'SUBARU'? Saya prediksi Salah.")
print(mobil.lower() == "SUBARU")

print("\n2c. Apakah mobil.lower() == 'SUBARU'.lower()? Saya prediksi Benar.")
print(mobil.lower() == "SUBARU".lower())

print("\n2d. Apakah 'Subaru'.lower() == 'subaru'? Saya prediksi Benar.")
print("Subaru".lower() == "subaru")

# ============================================================
# 3. Tes numerik
# ============================================================
umur = 25

print("\n3a. Apakah umur == 25? Saya prediksi Benar.")
print(umur == 25)

print("\n3b. Apakah umur == 30? Saya prediksi Salah.")
print(umur == 30)

print("\n3c. Apakah umur != 30? Saya prediksi Benar.")
print(umur != 30)

print("\n3d. Apakah umur != 25? Saya prediksi Salah.")
print(umur != 25)

print("\n3e. Apakah umur > 18? Saya prediksi Benar.")
print(umur > 18)

print("\n3f. Apakah umur > 30? Saya prediksi Salah.")
print(umur > 30)

print("\n3g. Apakah umur < 30? Saya prediksi Benar.")
print(umur < 30)

print("\n3h. Apakah umur < 18? Saya prediksi Salah.")
print(umur < 18)

print("\n3i. Apakah umur >= 25? Saya prediksi Benar.")
print(umur >= 25)

print("\n3j. Apakah umur >= 30? Saya prediksi Salah.")
print(umur >= 30)

print("\n3k. Apakah umur <= 25? Saya prediksi Benar.")
print(umur <= 25)

print("\n3l. Apakah umur <= 18? Saya prediksi Salah.")
print(umur <= 18)

# ============================================================
# 4. Tes menggunakan and / or
# ============================================================
print("\n4a. Apakah umur > 18 and umur < 65? Saya prediksi Benar.")
print(umur > 18 and umur < 65)

print("\n4b. Apakah umur > 18 and umur < 21? Saya prediksi Salah.")
print(umur > 18 and umur < 21)

print("\n4c. Apakah umur < 18 or umur > 21? Saya prediksi Benar.")
print(umur < 18 or umur > 21)

print("\n4d. Apakah umur < 18 or umur > 30? Saya prediksi Salah.")
print(umur < 18 or umur > 30)

print("\n4e. Apakah mobil == 'subaru' and umur == 25? Saya prediksi Benar.")
print(mobil == "subaru" and umur == 25)

print("\n4f. Apakah mobil == 'honda' or umur == 25? Saya prediksi Benar.")
print(mobil == "honda" or umur == 25)

# ============================================================
# 5. Tes apakah item ada di dalam list
# ============================================================
daftar_mobil = ["subaru", "toyota", "honda"]

print("\n5a. Apakah 'subaru' in daftar_mobil? Saya prediksi Benar.")
print("subaru" in daftar_mobil)

print("\n5b. Apakah 'audi' in daftar_mobil? Saya prediksi Salah.")
print("audi" in daftar_mobil)

# ============================================================
# 6. Tes apakah item TIDAK ada di dalam list
# ============================================================
print("\n6a. Apakah 'audi' not in daftar_mobil? Saya prediksi Benar.")
print("audi" not in daftar_mobil)

print("\n6b. Apakah 'subaru' not in daftar_mobil? Saya prediksi Salah.")
print("subaru" not in daftar_mobil)