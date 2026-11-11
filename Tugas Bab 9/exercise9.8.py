from privileges_admin import Admin

admin = Admin("Tyasanthi", "Elok", "tyasanthie", "tea@mail.com", "Cilacap")
admin.describe_user()
print()
admin.privileges.show_privileges()

# Tambahkan hak istimewa baru
admin.privileges.privileges.append("can reset password")
print("\nSetelah ditambah:")
admin.privileges.show_privileges()