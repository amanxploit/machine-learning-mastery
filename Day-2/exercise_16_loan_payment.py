# Exercise 16: Loan Payment Calculator
# ====================================
# REAL-LIFE SCENARIO: Mortgage, auto loans, student loans, credit cards
# WHY THIS MATTERS: Amortization = fixed payment series. Present value
#                   of annuity — fundamental in finance, RL reward discounting

# LEARNING OBJECTIVES:
# - Monthly payment formula (annuity formula)
# - Monthly rate = annual_rate / 12
# - Total paid = payment × months

# FORMULA (Monthly Payment):
# P = L × [r(1+r)ⁿ] / [(1+r)ⁿ - 1]
# P = monthly payment
# L = loan amount (principal)
# r = monthly interest rate (annual% / 100 / 12)
# n = total months (years × 12)

# YOUR TASK:
# 1. Ask loan amount (float)
# 2. Ask annual interest rate % (float)
# 3. Ask loan term in years (int)
# 4. Calculate monthly payment
# 5. Calculate total paid and total interest

# STEP-BY-STEP:
# 1. L = float(input("Loan amount: $"))
# 2. annual_pct = float(input("Annual rate %: "))
# 3. years = int(input("Years: "))
# 4. r = annual_pct / 100 / 12
# 5. n = years * 12
# 6. P = L * (r * (1+r)**n) / ((1+r)**n - 1)
# 7. total = P * n
# 8. interest = total - L
# 9. print(f"Monthly: ${P:.2f} | Total: ${total:.2f} | Interest: ${interest:.2f}")

# HINT: ** for exponentiation
# HINT: r is SMALL (e.g., 5% → 0.05/12 = 0.004167)
# HINT: Parentheses critical in formula!

# EXPECTED OUTPUT:
# Loan amount: $200000
# Annual rate %: 6.5
# Years: 30
# Monthly: $1264.14 | Total: $455090.40 | Interest: $255090.40

# EXTENSION CHALLENGES:
# - Amortization schedule (principal/interest per month)
# - Extra payment impact calculator
# - Affordability: given monthly budget, max loan?

print("=== Loan Payment Calculator ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")