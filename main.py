Reset = '\033[0m'
Red = '\033[31m'

Num1 = int(input("Please enter the first number: "))
Num2 = int(input("Please enter the second number: "))
Num3 = int(input("Please enter the third number: "))

if Num1 >= Num2 and Num1 >= Num3:
    print(f"{Red}{Num1}{Reset} is the largest of the 3 given numbers.")
elif Num2 >= Num1 and Num2 >= Num3:
    print(f"{Red}{Num2}{Reset} is the largest of the 3 given numbers.")
else:
    print(f"{Red}{Num3}{Reset} is the largest of the 3 given numbers.")