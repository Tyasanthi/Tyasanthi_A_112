#Tiga Cara Keluar dari Loop

#Versi A — kondisi di while (7-4)
topping = ""
while topping != "quit":
    topping = input("Topping (atau 'quit'): ")
    if topping != "quit":
        print(f"Menambahkan {topping}.")
#Penjelasan: Loop berhenti karena kondisi while menjadi False saat topping == "quit".

#Versi B — variabel aktif (7-4)
active = True
while active:
    topping = input("Topping (atau 'quit'): ")
    if topping == "quit":
        active = False
    else:
        print(f"Menambahkan {topping}.")
#Penjelasan: Variabel active mengontrol loop. Saat pengguna mengetik "quit", active diubah menjadi False, dan loop berhenti di iterasi berikutnya.

#Versi C — break (7-5)
while True:
    usia_input = input("Usia (atau 'quit'): ")
    if usia_input == "quit":
        break
    usia = int(usia_input)
    if usia < 3:
        print("Gratis.")
    elif usia <= 12:
        print("$10.")
    else:
        print("$15.")
#Penjelasan: break langsung keluar dari loop, mengabaikan kondisi while True.