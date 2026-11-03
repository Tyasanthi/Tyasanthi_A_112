cities = {
    "Jakarta": {
        "country": "Indonesia",
        "population": 10_500_000,
        "fact": "ibu kota negara dan pusat ekonomi",
    },
    "Tokyo": {
        "country": "Jepang",
        "population": 13_900_000,
        "fact": "kota terpadat di dunia",
    },
    "Paris": {
        "country": "Prancis",
        "population": 2_100_000,
        "fact": "terkenal dengan Menara Eiffel",
    },
}

for city, info in cities.items():
    print(f"\nKota: {city.title()}")
    print(f"  Negara    : {info['country'].title()}")
    print(f"  Populasi  : {info['population']:,}")
    print(f"  Fakta     : {info['fact']}")