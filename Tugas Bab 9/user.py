class User:
    """Merepresentasikan profil pengguna."""

    def __init__(self, first_name, last_name, username, email, lokasi):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.lokasi = lokasi
        self.login_attempts = 0

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"Nama lengkap : {self.first_name} {self.last_name}")
        print(f"Username     : {self.username}")
        print(f"Email        : {self.email}")
        print(f"Lokasi       : {self.lokasi}")

    def greet_user(self):
        """Menampilkan sapaan personal."""
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menambah percobaan login sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengembalikan percobaan login ke 0."""
        self.login_attempts = 0