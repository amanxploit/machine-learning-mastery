# Exercise 17: Investment Growth with Regular Contributions
# =========================================================
# REAL-LIFE SCENARIO: Retirement planning (401k, SIP), DCA investing
# WHY THIS MATTERS: Future value of annuity — compound growth + regular
#                   additions. Same math as gradient accumulation in ML!

# LEARNING OBJECTIVES:
# - Future Value of Annuity Due (contributions at period start)
# - Two components: lump sum growth + contribution growth
# - Time value of money with cash flows

# FORMULA:
# FV = P(1+r)ⁿ + PMT × [((1+r)ⁿ - 1) / r] × (1+r)
# FV = Future Value
# P = Initial principal
# PMT = Periodic contribution
# r = Periodic rate (annual% / 100 / frequency)
# n = Total periods (years × frequency)

# YOUR TASK:
# 1. Ask initial investment (float)
# 2. Ask monthly contribution (float)
# 3. Ask annual return % (float)
# 4. Ask years (int)
# 5. Calculate future value (monthly compounding)

# STEP-BY-STEP:
# 1. P = float(input("Initial investment: $"))
# 2. PMT = float(input("Monthly contribution: $"))
# 3. annual_pct = float(input("Annual return %: "))
# 4. years = int(input("Years: "))
# 5. r = annual_pct / 100 / 12
# 6. n = years * 12
# 7. fv_lump = P * (1 + r) ** n
# 8. fv_annuity = PMT * (((1 + r) ** n - 1) / r) * (1 + r)
# 9. fv = fv_lump + fv_annuity
# 10. total_contrib = P + PMT * n
# 11. gains = fv - total_contrib
# 12. print(f"Future Value: ${fv:.2f} | Contributed: ${total_contrib:.2f} | Gains: ${gains:.2f}")

# HINT: Monthly compounding = 12 periods/year
# HINT: (1+r) at end of annuity formula = annuity due (start of period)

# EXPECTED OUTPUT:
# Initial investment: $10000
# Monthly contribution: $500
# Annual return %: 8
# Years: 20
# Future Value: $334,572.45 | Contributed: $130,000.00 | Gains: $204,572.45

# EXTENSION CHALLENGES:
# - Inflation-adjusted return (real vs nominal)
# - Variable contribution increases yearly
# - Withdrawal phase (retirement drawdown)

print("=== Investment Growth Calculator ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")