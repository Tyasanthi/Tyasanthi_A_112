current_users =  ["Admin", "Tea", "Vrysa", "Kala", "Djilva"]
new_users = ["admin", "DESY", "Vrysa", "Windi", "Ganisa"]

#Salinan lowercase dari current_users untuk perbandingan case-insensitive
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah dipakai. Silakan pilih username lain.")
    else:
        print(f"Username '{new_user}' tersedia!")