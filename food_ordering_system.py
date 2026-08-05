# Food Ordering System
print("=" * 35)
print(" WELCOME TO APNA FOOD RESTAURANT")
print("=" * 35)
print("-" * 35)
print(" MENU LIST")
print("1. Burger  - RS 500")
print("2. Pizza   - RS 1200")
print("3. Fries   - RS 200")
print("4. Drink   - RS 100")
print("-" * 35)

choice = int(input("Select item (1-4): "))

# Step 1: Item & Price Assignment
if choice == 1:
    item_name = "Burger"
    price = 500
elif choice == 2:
    item_name = "Pizza"
    price = 1200
elif choice == 3:
    item_name = "Fries"
    price = 200
elif choice == 4:
    item_name = "Drink"
    price = 100
else:
    item_name = None
    price = 0

# Step 2: Order Processing
if item_name is not None:
    quantity = int(input(f"How many {item_name}s do you want? "))
    
    # Total Formula
    total_bill = price * quantity
    
    # Step 3: Receipt Print
    print("\n" + "=" * 35)
    print("           YOUR RECEIPT           ")
    print("=" * 35)
    print(f"Item Ordered : {item_name}")
    print(f"Price Per Unit: RS {price}")
    print(f"Quantity     : {quantity}")
    print("-" * 35)
    print(f"Total Bill   : RS {total_bill}")
    print("=" * 35)
else:
    print("\nInvalid Choice! Please select between 1 and 4.")
