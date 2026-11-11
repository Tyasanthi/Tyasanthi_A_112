from user import User

class Admin(User):
    """Administrator adalah jenis User khusus."""

    def __init__(self, first_name, last_name, username, email, lokasi):
        super().__init__(first_name, last_name, username, email, lokasi)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can edit post",
        ]

    def show_privileges(self):
        """Menampilkan daftar hak istimewa administrator."""
        print("Hak istimewa administrator:")
        for p in self.privileges:
            print(f"  - {p}")