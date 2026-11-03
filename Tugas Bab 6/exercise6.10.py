favorite_numbers = {
    "TEA": [7, 14],
    "Kayla": [21, 2],
    "Djilva": [13, 42, 8],
    "Vrysa": [5, 10],
    "Desy": [1, 2, 3],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} punya angka favorit:")
    for number in numbers:
        print(f"  - {number}")