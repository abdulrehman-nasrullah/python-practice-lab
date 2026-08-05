# Student Result Management

sub1 = float(input("Enter Subject 1 marks (out of 100): "))
sub2 = float(input("Enter Subject 2 marks (out of 100): "))
sub3 = float(input("Enter Subject 3 marks (out of 100): "))
sub4 = float(input("Enter Subject 4 marks (out of 100): "))
sub5 = float(input("Enter Subject 5 marks (out of 100): "))

total_marks = sub1+sub2+sub3+sub4+sub5

percentage = (total_marks * 100) / 500


if percentage >=90:
    print("Grade A+")
elif percentage >=80:
    print("Grade A")
elif percentage >=70:
    print("Grade B")
elif percentage >=60:
    print("Grade B")
else:
    print("You Fail") 

print(f"Your total marks are {total_marks} / out of 500")
print(f"Your percentage is {percentage}%")