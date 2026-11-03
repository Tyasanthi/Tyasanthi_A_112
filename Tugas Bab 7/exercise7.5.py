print("Masukkan usia untuk mengetahui harga tiket (ketik 'quit' untuk berhenti):")

while True:
    usia_input = input("Usia: ")
    if usia_input == "quit":
        break
    usia = int(usia_input)
    if usia < 3:
        print("Tiket gratis.")
    elif usia <= 12:
        print("Harga tiket: $10.")
    else:
        print("Harga tiket: $15.")