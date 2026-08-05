print("=" * 30)
print(" Mobile Package Selector")
print("=" * 30)
print("1. Daily")
print("2. Weekly")
print("3. Monthly")

choice = int(input("Select your package (1, 2, 3): "))

if choice == 1:
    package_name = "Daily"
    price = 50
elif choice == 2:
    package_name = "Weekly"
    price = 250
elif choice == 3:
    package_name = "Monthly"
    price = 800
else:
    package_name = None

# Print Result
if package_name:
    print(f"{package_name} Package Price is RS {price}")
else:
    print("Invalid package selection!")