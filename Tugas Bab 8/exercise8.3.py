def make_shirt(size, message):
    print(f"Kaos ukuran {size} dengan pesan: '{message}'.")

# Argumen posisional (urutan harus sesuai)
make_shirt("XXL", "I <3 Buna")

# Argumen keyword (urutan bebas, lebih jelas)
make_shirt(message="I <3 Wowo", size="XXXL")