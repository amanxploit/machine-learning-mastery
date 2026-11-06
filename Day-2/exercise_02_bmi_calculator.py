# Exercise 2: BMI Calculator
# ===========================
# REAL-LIFE SCENARIO: Health apps, fitness trackers, medical screening
# WHY THIS MATTERS: Feature engineering — BMI is a derived feature from
#                   height/weight. ML models often need computed features.

# LEARNING OBJECTIVES:
# - Practice float arithmetic with exponents ( ** )
# - Understand formula translation to code
# - Categorize numeric results into labels

# FORMULA:
# BMI = weight_kg / (height_m ** 2)
# OR  BMI = (weight_lbs / (height_in ** 2)) * 703

# CATEGORIES (WHO Standard):
# Underweight:  BMI < 18.5
# Normal:       18.5 ≤ BMI < 25
# Overweight:   25 ≤ BMI < 30
# Obese:        BMI ≥ 30

# YOUR TASK:
# 1. Ask for weight in kg (float)
# 2. Ask for height in meters (float) — e.g., 1.75
# 3. Calculate BMI
# 4. Determine category using if/elif/else (Day 3 preview)
# 5. Print BMI with 1 decimal and category

# STEP-BY-STEP:
# 1. weight = float(input("Weight (kg): "))
# 2. height = float(input("Height (m): "))
# 3. bmi = weight / (height ** 2)
# 4. Use if/elif/else for category
# 5. print(f"BMI: {bmi:.1f} — Category: {category}")

# HINT: ** is exponent operator (height ** 2 = height²)
# HINT: Parentheses matter: weight / (height ** 2) NOT weight / height ** 2

# EXPECTED OUTPUT:
# Weight (kg): 70
# Height (m): 1.75
# BMI: 22.9 — Category: Normal

# EXTENSION CHALLENGES:
# - Accept height in cm (convert to m: cm / 100)
# - Accept weight in lbs (convert to kg: lbs / 2.205)
# - Calculate ideal weight range for given height

print("=== BMI Calculator ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")