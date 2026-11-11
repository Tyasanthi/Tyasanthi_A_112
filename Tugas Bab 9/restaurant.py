class Restaurant:
    """Merepresentasikan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Menyimpan nama restoran dan jenis masakan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        """Menampilkan informasi restoran."""
        print(f"Nama Restoran : {self.restaurant_name}")
        print(f"Jenis Masakan : {self.cuisine_type}")

    def open_restaurant(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} sekarang BUKA! Selamat datang.")

    def set_number_served(self, jumlah):
        """Menetapkan jumlah pelanggan yang telah dilayani."""
        self.number_served = jumlah

    def increment_number_served(self, tambahan):
        """Menambah jumlah pelanggan yang telah dilayani."""
        self.number_served += tambahan

class IceCreamStand(Restaurant):
    """Stand es krim adalah jenis restoran khusus."""

    def __init__(self, restaurant_name, cuisine_type="Es Krim"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Cokelat", "Vanila", "Stroberi", "Mangga", "Matcha"]

    def tampilkan_flavors(self):
        """Menampilkan daftar rasa es krim."""
        print(f"\nRasa es krim yang tersedia di {self.restaurant_name}:")
        for rasa in self.flavors:
            print(f"  - {rasa}")