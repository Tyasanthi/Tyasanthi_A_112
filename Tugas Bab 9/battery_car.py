class Battery:
    """Model baterai untuk mobil listrik."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki baterai {self.battery_size}-kWh.")

    def get_range(self):
        """Menampilkan perkiraan jarak tempuh."""
        if self.battery_size == 40:
            range_km = 150
        elif self.battery_size == 65:
            range_km = 225
        else:
            range_km = self.battery_size * 3.75
        print(f"Mobil ini dapat menempuh sekitar {int(range_km)} km dengan baterai penuh.")

    def upgrade_battery(self):
        """Meningkatkan kapasitas baterai menjadi 65 jika belum."""
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar:
    """Representasi mobil listrik."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"