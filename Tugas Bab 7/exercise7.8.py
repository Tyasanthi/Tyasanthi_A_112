sandwich_orders = ["tuna", "ham", "veggie", "turkey", "club"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Saya membuat sandwich {sandwich} Anda.")
    finished_sandwiches.append(sandwich)

print("\nSemua sandwich sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"  - {sandwich}")