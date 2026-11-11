# Pengujian fungsi get_city_country().

from city_functions import get_city_country


def test_city_country():
    """Apakah 'santiago' + 'chile' menghasilkan 'Santiago, Chile'?"""
    hasil = get_city_country("santiago", "chile")
    assert hasil == "Santiago, Chile"


def test_city_country_population():
    """Apakah 'santiago' + 'chile' + 5000000 menghasilkan format lengkap?"""
    hasil = get_city_country("santiago", "chile", population=5000000)
    assert hasil == "Santiago, Chile - populasi 5000000"