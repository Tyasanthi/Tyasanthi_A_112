cities = {
    "Jakarta": {
        "country": "Indonesia",
        "population": 10_500_000,
        "fact": "ibu kota negara dan pusat ekonomi",
        "language": "Indonesia",
        "currency": "rupiah",
    },
    "Tokyo": {
        "country": "Jepang",
        "population": 13_900_000,
        "fact": "kota terpadat di dunia",
        "language": "Jepang",
        "currency": "yen",
    },
    "Paris": {
        "country": "Prancis",
        "population": 2_100_000,
        "fact": "terkenal dengan Menara Eiffel",
        "language": "Prancis",
        "currency": "euro",
    },
}

print("=" * 50)
print(f"{'INFORMASI KOTA':^50}")
print("=" * 50)

for city, info in cities.items():
    print(f"\n🏙  {city.title()}")
    print("-" * 50)
    for key, value in info.items():
        label = key.replace("_", " ").title()
        if key == "population":
            value = f"{value:,} jiwa"
        print(f"  {label:<12}: {value}")

# Statistik tambahan
total_population = sum(info["population"] for info in cities.values())
print("\n" + "=" * 50)
print(f"Total populasi ketiga kota: {total_population:,} jiwa")
print(f"Kota terpadat: {max(cities, key=lambda c: cities[c]['population']).title()}")