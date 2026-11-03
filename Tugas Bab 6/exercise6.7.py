person_1 = {
    "first_name": "Tyasanthi",
    "last_name": "Adiutami",
    "age": 18,
    "city": "Cilacap",
}
person_2 = {
    "first_name": "Kayla",
    "last_name": "Nafisa",
    "age": 11,
    "city": "Bandung",
}
person_3 = {
    "first_name": "Djilva",
    "last_name": "Wijaya",
    "age": 35,
    "city": "Surabaya",
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\nNama lengkap: {person['first_name']} {person['last_name']}")
    print(f"Usia        : {person['age']}")
    print(f"Kota        : {person['city']}")