from user import User

class Privileges:
    """Menyimpan daftar hak istimewa (privileges)."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "can add post",
                "can delete post",
                "can ban user",
                "can edit post",
            ]
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak istimewa."""
        print("Hak istimewa administrator:")
        for p in self.privileges:
            print(f"  - {p}")


class Admin(User):
    """Administrator adalah jenis User khusus."""

    def __init__(self, first_name, last_name, username, email, lokasi):
        super().__init__(first_name, last_name, username, email, lokasi)
        self.privileges = Privileges()