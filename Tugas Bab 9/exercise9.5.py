from user import User

u = User("Tyasanthi", "Elok", "tyasanthie", "tea@mail.com", "Cilacap")

for _ in range(5):
    u.increment_login_attempts()
print(f"Login attempts setelah 5 kali increment : {u.login_attempts}")

u.reset_login_attempts()
print(f"Login attempts setelah reset            : {u.login_attempts}")