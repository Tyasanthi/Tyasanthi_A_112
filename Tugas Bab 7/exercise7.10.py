responses = {}
polling_active = True

print("Selamat datang di polling liburan impian!")

while polling_active:
    nama = input("\nSiapa nama Anda? (ketik 'quit' untuk berhenti): ")
    if nama == "quit":
        polling_active = False
        continue

    tempat = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")
    responses[nama] = tempat
    print(f"Terima kasih, {nama.title()}! Jawaban Anda sudah dicatat.")

# Tampilkan hasil polling
print("\n" + "=" * 40)
print("HASIL POLLING LIBURAN IMPIAN")
print("=" * 40)

for nama, tempat in responses.items():
    print(f"{nama.title()} ingin pergi ke {tempat.title()}.")