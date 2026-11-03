#Tiga contoh program yang sudah sesuai PEP 8:

#(a) 8-2 Buku Favorit
def favorite_book(title):
    """Menampilkan pesan tentang buku favorit."""
    print(f"Salah satu buku favorit saya adalah {title.title()}.")


favorite_book("Lord of the Flies")

#(b) 8-6 Nama Kota
def city_country(city, country):
    """Mengembalikan string 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"

print(city_country("Berlin", "Jerman"))
print(city_country("Bandung", "Indonesia"))
print(city_country("Paris", "Prancis"))

#(c) 8-14 Mobil
def make_car(manufacturer, model, **options):
    """Membuat dictionary berisi info mobil."""
    car = {"manufacturer": manufacturer, "model": model}
    car.update(options)
    return car


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)