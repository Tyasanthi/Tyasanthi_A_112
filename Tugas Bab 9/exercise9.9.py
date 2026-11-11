from battery_car import ElectricCar

car = ElectricCar("Tesla", "Model 3", 2024)
print(car.get_descriptive_name())
car.battery.describe_battery()
car.battery.get_range()           # range awal

print("\n>>> Melakukan upgrade baterai...")
car.battery.upgrade_battery()
car.battery.describe_battery()
car.battery.get_range()           # range setelah upgrade