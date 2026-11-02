pizzaku = ["pepperoni", "margherita", "hawaiian"]
pizza_teman = pizzaku[:]        # salinan (copy), jadi nanti merujuk ke list yang berbeda, tanda [:] penting!
#cara lain pakai: pizzaku.copy() atau list(pizzaku)

# Tambah pizza baru ke masing-masing list
pizzaku.append("bbq chicken")
pizza_teman.append("veggie")

# Buktikan dua list terpisah
print("Pizza favoritku adalah: ")
for pizza in pizzaku:
    print(f"{pizza}")

print("\nPizza favorit temanku adalah: ")
for pizza in pizza_teman:
    print(f"{pizza}")