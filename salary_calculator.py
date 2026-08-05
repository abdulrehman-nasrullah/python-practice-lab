# Salary Calculator
basic_salary = float(input("Enter your salary: "))
bonus = float(input("Enter your bonus: "))
tax_percentage = float(input("Enter your tax (%): "))

# # Calculations
gross_salary = basic_salary + bonus
tax_amount = (gross_salary * tax_percentage) / 100  # Fix here
net_salary = gross_salary - tax_amount

# Print Output
print(f"Gross Salary is {gross_salary:.2f}")
print(f"Tax Amount is {tax_amount:.2f}")
print(f"Net Salary is {net_salary:.2f}")
