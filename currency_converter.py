# Currency Converter
rate = 285
print("PKR to USD")
print("USD to PKR")

choice = int(input("Select (1 or 2): "))
if choice == 1:
    amount = float(input("Enter PKR amount: "))
    converted_amonut = amount/rate
    print(f"USD is $:{converted_amonut}")
elif choice == 2:
    amount = float(input("Enter USD amount: "))
    converted_amonut = amount * rate
    print(f"PKR is RS:{converted_amonut}")