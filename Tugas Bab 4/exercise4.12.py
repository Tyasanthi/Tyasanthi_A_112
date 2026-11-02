makananku = ["mie ayam", "soto", "sate"]
makanan_teman = makananku[:]

makananku.append("bakso")
makanan_teman.append("es krim")

print("Makanan favoritku yaitu: ")
for makanan in makananku:
    print(f"{makanan}")

print("\nMakanan favorit temanku yaitu: ")
for makanan in makanan_teman:
    print(f"{makanan}")