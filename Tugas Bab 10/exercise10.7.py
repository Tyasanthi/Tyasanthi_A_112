# 10-7_addition_calculator.py
# Program penjumlahan dengan while loop; bisa lanjut walau salah input.

print("Kalkulator Penjumlahan - ketik 'q' untuk keluar.")
print("=" * 50)

while True:
    try:
        angka1 = input("Masukkan angka pertama : ")
        if angka1.lower() == "q":
            break
        angka1 = int(angka1)

        angka2 = input("Masukkan angka kedua   : ")
        if angka2.lower() == "q":
            break
        angka2 = int(angka2)
    except ValueError:
        print("!! Input tidak valid. Silakan masukkan angka.\n")
    else:
        hasil = angka1 + angka2
        print(f"  Hasil: {angka1} + {angka2} = {hasil}\n")

print("Sampai jumpa!")