# Kelas Employee untuk menyimpan data karyawan.

class Employee:
    """Merepresentasikan seorang karyawan."""

    def __init__(self, nama_depan, nama_belakang, gaji_tahunan):
        """Menyimpan nama dan gaji tahunan karyawan."""
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.gaji_tahunan = gaji_tahunan

    def give_raise(self, kenaikan=5000):
        """Menambah gaji tahunan.

        Default: $5.000. Bisa juga menerima nominal kenaikan lain.
        """
        self.gaji_tahunan += kenaikan