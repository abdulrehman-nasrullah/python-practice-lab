# Car Parking Fee Calculator
hours = float(input("Enter hours to check parking fee: "))
if hours <=2:
    print("Parking fee is RS 100")
elif hours >=3 and hours<=5:
    print("Parking fee is RS 200")
else:
    print("Parking fee is RS 500")
