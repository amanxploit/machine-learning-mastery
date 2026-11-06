# Exercise 11: Percentage Change Calculator
# =========================================
# REAL-LIFE SCENARIO: Stock markets, sales analytics, A/B testing, ML metrics
# WHY THIS MATTERS: % change = (new - old) / |old| × 100 — used everywhere:
#                   loss curves, accuracy improvement, data drift detection

# LEARNING OBJECTIVES:
# - Percentage change formula
# - Handling increase vs decrease (sign matters!)
# - Absolute value concept

# FORMULA:
# % Change = ((New - Old) / |Old|) × 100
# Positive = increase, Negative = decrease

# YOUR TASK:
# 1. Ask for original value (float)
# 2. Ask for new value (float)
# 3. Calculate % change
# 4. Print with sign (+/-) and "increase"/"decrease"

# STEP-BY-STEP:
# 1. old = float(input("Original value: "))
# 2. new = float(input("New value: "))
# 3. change = ((new - old) / abs(old)) * 100
# 4. direction = "increase" if change >= 0 else "decrease"
# 5. print(f"Change: {change:+.2f}% ({direction})")
#    # +.2f shows + for positive, - for negative

# HINT: abs() = absolute value (removes negative sign)
# HINT: +.2f format shows explicit + sign for positive numbers

# EXPECTED OUTPUT:
# Original value: 50
# New value: 75
# Change: +50.00% (increase)

# Original value: 80
# New value: 60
# Change: -25.00% (decrease)

# EXTENSION CHALLENGES:
# - Calculate new value given original and % change
# - Compound % changes (sequential increases/decreases)
# - Year-over-year growth rate

print("=== Percentage Change Calculator ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")