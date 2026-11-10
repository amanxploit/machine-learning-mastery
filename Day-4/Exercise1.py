

operator = input("Enter your operator (+,-,/,*): ")

num1 = float(input("Enter Your 1st Number: "))
num2 = float(input("Enter Your 2nd Number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
else:
    print(f"{operator} is not valid")