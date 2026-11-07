# Exercise 4: Tip Calculator with Bill Split
# ===========================================
# REAL-LIFE SCENARIO: Restaurant apps, group dining, expense sharing
# WHY THIS MATTERS: Proportional division, percentage math — essential for
#                   data splitting (train/test), sampling, weighted averages

# LEARNING OBJECTIVES:
# - Percentage calculations (tip = bill × rate)
# - Division with rounding considerations
# - Multi-step arithmetic workflow

# YOUR TASK:
# 1. Ask for bill total (float)
# 2. Ask for tip percentage (float, e.g., 18 for 18%)
# 3. Ask for number of people (int)
# 4. Calculate tip amount
# 5. Calculate total with tip
# 6. Calculate per-person share
# 7. Print all values with 2 decimals

# STEP-BY-STEP:
# 1. bill = float(input("Bill total: $"))
# 2. tip_pct = float(input("Tip %: "))
# 3. people = int(input("Number of people: "))
# 4. tip = bill * (tip_pct / 100)
# 5. total = bill + tip
# 5. share = total / people
# 6. print(f"Tip: ${tip:.2f} | Total: ${total:.2f} | Each: ${share:.2f}")

# HINT: tip_pct / 100 converts 18 → 0.18
# HINT: Division of money — consider rounding issues in real apps

# EXPECTED OUTPUT:
# Bill total: $85.50
# Tip %: 20
# Number of people: 4
# Tip: $17.10 | Total: $102.60 | Each: $25.65

# EXTENSION CHALLENGES:
# - Handle uneven split (some pay more/less)
# - Add tax calculation before tip
# - Round per-person to nearest $0.05 (cash-friendly)

print("=== Tip Calculator ===")
# YOUR CODE BELOW THIS LINE

bill = float(input("Bill total: $"))
tip_pct = float(input("Tip %: "))
people = int(input("Number of people: "))

tip = bill * (tip_pct / 100)
total = bill + tip
share = total / people

print(f"Tip: ${tip:.2f} | Total: ${total:.2f} | Each: ${share:.2f}")

# YOUR CODE ABOVE THIS LINE
print("=== Done ===")