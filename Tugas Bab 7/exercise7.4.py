print("Masukkan topping pizza (ketik 'quit' untuk berhenti):")

while True:
    topping = input("Topping: ")
    if topping == "quit":
        break
    print(f"Saya akan menambahkan {topping} ke pizza Anda.")