from restaurant import Restaurant

restaurant = Restaurant("Warung Sederhana", "Indonesia")

print("Atribut secara individual:")
print(f"  Nama  : {restaurant.restaurant_name}")
print(f"  Jenis : {restaurant.cuisine_type}")

print("\nMemanggil describe_restaurant():")
restaurant.describe_restaurant()

print("\nMemanggil open_restaurant():")
restaurant.open_restaurant()