#===================================
# 1. Membuat list
#===================================
gunung = ["Bromo", "Rinjani", "Krakatau", "Jayawijaya", "Kilimanjaro"]
print("1. List awal: ")
print(gunung)

#===================================
# 2. Mengakses elemen (indexing)
#===================================
print("\n2. Mengakses elemen:")
print(f"   Gunung pertama: {gunung[0]}")
print(f"   Gunung terakhir: {gunung[-1]}")

#===================================
# 3. Mengubah elemen (assignment)
#===================================
gunung[2] = "Merapi"   #diganti Merapi
print("\n3. Setelah mengubah elemen indeks 2: ")
print(gunung)

#===================================
# 4. append() — menambah di akhir
#===================================
gunung.append("Lawu")
print("\n4. Setelah append('Lawu'): ")
print(gunung)

#===================================
# 5. insert() — menyisipkan di posisi tertentu
#===================================
gunung.insert(0, "Sumbing")
print("\n5. Setelah insert(0, 'Sumbing'): ")
print(gunung)

#===================================
# 6. del — menghapus berdasarkan indeks
#===================================
del gunung[1]   # hapus "Everest"
print("\n6. Setelah del gunung[1]:")
print(gunung[1]) #hapus Bromo
print("\n6. Setelah del gunung[1]: ")
print(gunung)

#===================================
# 7. pop() — menghapus & mengembalikan elemen terakhir
#===================================
hapus = gunung.pop()
print(f"\n7. Setelah pop() — yang dihapus: {hapus}")
print(gunung)

#===================================
# 8. pop(0) — menghapus & mengembalikan elemen pertama
#===================================
hapus_pertama = gunung.pop(0)
print(f"\n8. Setelah pop(0) — yang dihapus: {hapus_pertama}")
print(gunung)

#===================================
# 9. remove() — menghapus berdasarkan nilai
#===================================
gunung.remove("Rinjani")
print("\n9. Setelah remove('Rinjani'): ")
print(gunung)

#===================================
# 10. len() — menghitung jumlah elemen
#===================================
print(f"\n10. Jumlah gunung dalam list: {len(gunung)}")

#===================================
# 11. sorted() — urutan alfabetis TANPA mengubah list
#===================================
print("\n11. sorted() — alfabetis (list tidak berubah): ")
print(sorted(gunung))
print("List asli masih:")
print(gunung)

#===================================
# 12. sorted(reverse=True) — alfabetis terbalik TANPA mengubah list
#===================================
print("\n12. sorted(reverse=True) — alfabetis terbalik (list tidak berubah): ")
print(sorted(gunung, reverse=True))
print("List asli masih: ")
print(gunung)

#===================================
# 13. reverse() — membalik urutan list secara permanen
#===================================
gunung.reverse()
print("\n13. Setelah reverse():")
print(gunung)

#===================================
# 14. sort() — mengurutkan list secara permanen (alfabetis)
#===================================
gunung.sort()
print("\n14. Setelah sort() — alfabetis: ")
print(gunung)

#===================================
# 15. sort(reverse=True) — mengurutkan permanen (terbalik)
#===================================
gunung.sort(reverse=True)
print("\n15. Setelah sort(reverse=True) — alfabetis terbalik: ")
print(gunung)