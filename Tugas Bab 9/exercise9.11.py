from privileges_admin import Admin

admin = Admin("Fajar", "Nugroho", "fajarn", "fajar@mail.com", "Medan")
admin.describe_user()
print()
admin.privileges.show_privileges()