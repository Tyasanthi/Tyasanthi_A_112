def build_profile(first, last, **user_info):
    profile = {"first_name": first, "last_name": last}
    profile.update(user_info)
    return profile

user_profile = build_profile(
    "Tyasanthi", "Adiutami",
    lokasi="Surakarta",
    bidang="Teknik Industri",
    hobi="Membaca"
)
print(user_profile)