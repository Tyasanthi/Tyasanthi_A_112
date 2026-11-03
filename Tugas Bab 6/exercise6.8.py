pet_1 = {"kind": "anjing", "owner": "Tea"}
pet_2 = {"kind": "kucing", "owner": "Djilva"}
pet_3 = {"kind": "kelinci", "owner": "Kayla"}
pet_4 = {"kind": "burung", "owner": "Vrysa"}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"{pet['owner'].title()} memelihara seekor {pet['kind']}.")