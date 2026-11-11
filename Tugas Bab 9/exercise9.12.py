from privileges_admin import Admin

admin = Admin("Gita", "Lestari", "gital", "gita@mail.com", "Makassar")
admin.describe_user()
print()
admin.privileges.show_privileges()