import random

class Die:
    """Representasi dadu."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Menampilkan angka acak antara 1 dan jumlah sisi."""
        hasil = random.randint(1, self.sides)
        print(hasil, end=" ")
        return hasil