# Pengujian kelas Employee — versi final dengan fixture.

import pytest
from employee import Employee


@pytest.fixture
def karyawan():
    """Fixture: menyediakan instance Employee yang siap pakai.

    Menghindari pembuatan ulang di setiap test function.
    """
    return Employee("Andi", "Wijaya", 50000)


def test_give_default_raise(karyawan):
    """Kenaikan default harus menambah $5.000 ke gaji."""
    karyawan.give_raise()
    assert karyawan.gaji_tahunan == 55000


def test_give_custom_raise(karyawan):
    """Kenaikan kustom (misal $10.000) harus menambah sesuai nominal."""
    karyawan.give_raise(10000)
    assert karyawan.gaji_tahunan == 60000