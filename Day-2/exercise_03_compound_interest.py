# Exercise 3: Compound Interest Calculator
# ========================================
# REAL-LIFE SCENARIO: Banking, investments, savings planning, loan analysis
# WHY THIS MATTERS: Exponential growth modeling — core concept in ML
#                   (compounding = exponential; gradients = rates of change)

# LEARNING OBJECTIVES:
# - Practice exponentiation with ** operator
# - Understand time-value of money mathematics
# - Work with percentages as decimals (5% = 0.05)

# FORMULA:
# A = P(1 + r/n)^(nt)
# A = Final amount
# P = Principal (initial investment)
# r = Annual interest rate (as decimal: 5% → 0.05)
# n = Compounds per year (12=monthly, 4=quarterly, 1=annual)
# t = Years

# YOUR TASK:
# 1. Ask for principal amount (float)
# 2. Ask for annual interest rate % (float, e.g., 5 for 5%)
# 3. Ask for years (int)
# 4. Ask for compound frequency (int: 1, 4, 12, 365)
# 5. Calculate final amount
# 6. Calculate total interest earned (A - P)
# 7. Print both with 2 decimals

# STEP-BY-STEP:
# 1. p = float(input("Principal: $"))
# 2. r_pct = float(input("Annual rate (%): "))
# 3. r = r_pct / 100          # Convert % to decimal
# 4. t = int(input("Years: "))
# 5. n = int(input("Compounds/year (1/4/12/365): "))
# 6. a = p * (1 + r/n) ** (n*t)
# 7. interest = a - p
# 8. print(f"Final: ${a:.2f}, Interest: ${interest:.2f}")

# HINT: Convert percentage FIRST: 5% → 0.05
# HINT: ** has higher precedence than * — parentheses are correct as written

# EXPECTED OUTPUT:
# Principal: $1000
# Annual rate (%): 5
# Years: 10
# Compounds/year (1/4/12/365): 12
# Final: $1647.01, Interest: $647.01

# EXTENSION CHALLENGES:
# - Calculate how long to double money (Rule of 72: 72/rate)
# - Add monthly contribution option (annuity formula)
# - Compare simple vs compound interest

print("=== Compound Interest Calculator ===")
# YOUR CODE BELOW THIS LINE

p = float(input("Principal: $"))
r_pct = float(input("Annual rate (%): "))
r = r_pct / 100
t = int(input("Years: "))
n = int(input("Compounds/year (1/4/12/365): "))
a = p * (1 + r/n) ** (n*t)
interest = a - p
print(f"Final: ${a:.2f}, Interest: ${interest:.2f}")

# YOUR CODE ABOVE THIS LINE
print("=== Done ===")