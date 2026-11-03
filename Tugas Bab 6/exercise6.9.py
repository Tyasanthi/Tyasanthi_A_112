favorite_places = {
    "TEA": ["Jerman", "Bali", "Semarang"],
    "Djilva": ["Bandung", "Danau Toba"],
    "Kala": ["Labuan Bajo"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} suka mengunjungi:")
    for place in places:
        print(f"  - {place}")