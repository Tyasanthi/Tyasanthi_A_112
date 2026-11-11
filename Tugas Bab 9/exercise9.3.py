from user import User

user1 = User("Tyasanthi", "Elok", "tyasanthie", "tea@mail.com", "Cilacap")
user2 = User("Djilva", "Raihanun", "djilvar", "djil@mail.com", "Bandung")
user3 = User("Desy", "Ayu", "desya", "des@mail.com", "Surabaya")

for u in (user1, user2, user3):
    u.describe_user()
    u.greet_user()
    print("-" * 30)