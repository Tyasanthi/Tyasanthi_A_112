# Fungsi untuk membentuk string "Kota, Negara".

def get_city_country(city, country, population=None):
    """Mengembalikan string berbentuk 'Kota, Negara'.

    Jika population diberikan, tambahkan keterangan populasi.
    Parameter population bersifat OPSIONAL (latihan 11-2).
    """
    if population:
        return f"{city.title()}, {country.title()} - populasi {population}"
    return f"{city.title()}, {country.title()}"