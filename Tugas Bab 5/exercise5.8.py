usernames = ["admin", "Tea", "Vrysa", "Kala", "Djilva"]

for username in usernames:
    if username == "admin":
        print("Halo admin, apakah kamu ingin melihat laporan status?")
    else:
        print(f"Halo {username.title()}, terima kasih sudah login kembali.")