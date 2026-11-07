# Exercise 1: Temperature Converter (Celsius ↔ Fahrenheit)
# =========================================================
# REAL-LIFE SCENARIO: Weather apps, cooking, science experiments
# WHY THIS MATTERS: Unit conversion is fundamental in data preprocessing for ML
#                   (e.g., normalizing sensor data from different sources)

# LEARNING OBJECTIVES:
# - Practice float arithmetic with formulas
# - Understand order of operations (parentheses matter!)
# - Build reusable conversion logic

# FORMULAS:
# Celsius to Fahrenheit:  F = (C × 9/5) + 32
# Fahrenheit to Celsius:  C = (F - 32) × 5/9

# YOUR TASK:
# 1. Ask user for temperature value (float)
# 2. Ask user for unit: 'C' for Celsius or 'F' for Fahrenheit
# 3. Convert to the other unit
# 4. Print result with 2 decimal places

# STEP-BY-STEP:
# 1. temp = float(input("Enter temperature: "))
# 2. unit = input("Enter unit (C/F): ").upper()
# 3. Use if/else (preview of Day 3!) or just do both conversions
# 4. Print: f"{temp}°{unit} = {converted:.2f}°{other_unit}"

# HINT: .upper() converts 'c' → 'C', 'f' → 'F'
# HINT: :.2f formats to 2 decimal places

# EXPECTED OUTPUT:
# Enter temperature: 100
# Enter unit (C/F): C
# 100.00°C = 212.00°F

# EXTENSION CHALLENGES:
# - Add Kelvin conversion: K = C + 273.15
# - Handle invalid unit input gracefully
# - Create a menu loop (after learning loops)

print("=== Temperature Converter ===")
# YOUR CODE BELOW THIS LINE

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp:.2f}°F = {converted:.2f}°C")
elif unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp:.2f}°C = {converted:.2f}°F")
else:
    print(f"Error: '{unit}' is not a valid unit. Use 'C' or 'F'.")

# YOUR CODE ABOVE THIS LINE
print("=== Done ===")