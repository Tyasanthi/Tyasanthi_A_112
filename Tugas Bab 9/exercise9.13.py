from die import Die

print("Dadu 6 sisi, dilempar 10 kali:")
d6 = Die()
for _ in range(10):
    d6.roll_die()
print("\n")

print("Dadu 10 sisi, dilempar 10 kali:")
d10 = Die(sides=10)
for _ in range(10):
    d10.roll_die()
print("\n")

print("Dadu 20 sisi, dilempar 10 kali:")
d20 = Die(sides=20)
for _ in range(10):
    d20.roll_die()
print()