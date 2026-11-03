rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}

# Kalimat tentang setiap sungai
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Nama setiap sungai
print("\nNama sungai:")
for river in rivers.keys():
    print(f"  {river.title()}")

# Nama setiap negara
print("\nNama negara:")
for country in rivers.values():
    print(f"  {country.title()}")