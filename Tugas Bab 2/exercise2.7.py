nama = "\t\n Wowo Teddy \n\t"

print("Original (ada Whitespace):")
print(repr(nama))
print(nama)

print("\npakai lstrip():")
print(f"[{nama.lstrip()}]")

print("\npakai rstrip():")
print(f"[{nama.rstrip()}]")

print("\npakai strip():")
print(f"[{nama.strip()}]")