# Temperature Converison

temp = float(input("Enter your Temperature?: "))
unit = input("Is this temperature is Celsius or Fahrenheit(C/F)?: ").capitalize()

if unit=="C":
    temp = round((9*temp)/5+32,1)
    unit="F"
    print(f"The Temperature in Fahrenheit: {temp}{unit}")
elif unit=="F":
    temp = round((temp-32) *5 /9,1)
    unit="C"
    print(f"The Temperature in Celsius: {temp}{unit}")
else:
    print(f"{unit} is an invalid unit of measurement")


