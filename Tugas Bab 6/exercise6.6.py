favorite_languages = {
    "TEA": "python",
    "Djilva": "javascript",
    "Kala": "rust",
    "Vrysa": "go",
}

people_to_poll = ["TEA", "Desy", "Djilva", "Lana", "Vrysa"]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Terima kasih, {person.title()}, sudah mengikuti polling!")
    else:
        print(f"Halo {person.title()}, silakan ikut polling bahasa favorit!")