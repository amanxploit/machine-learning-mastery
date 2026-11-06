# Exercise 12: Discount & Sale Price
# ==================================
# REAL-LIFE SCENARIO: E-commerce, retail, coupon systems, pricing engines
# WHY THIS MATTERS: Reverse percentage — given final price and discount,
#                   find original. Inverse problem solving (like ML inference!)

# LEARNING OBJECTIVES:
# - Forward: Sale = Original × (1 - discount%)
# - Reverse: Original = Sale / (1 - discount%)
# - Percentage as decimal multiplier

# YOUR TASK:
# Menu:
# 1) Find sale price (given original + discount%)
# 2) Find original price (given sale + discount%)
# 3) Find discount % (given original + sale)

# STEP-BY-STEP:
# 1. print("1) Sale Price  2) Original Price  3) Discount %")
# 2. choice = int(input("Choose: "))
# 3. if choice == 1:
#       orig = float(input("Original: $"))
#       pct = float(input("Discount %: "))
#       sale = orig * (1 - pct/100)
#       print(f"Sale: ${sale:.2f}")
#    elif choice == 2:
#       sale = float(input("Sale: $"))
#       pct = float(input("Discount %: "))
#       orig = sale / (1 - pct/100)
#       print(f"Original: ${orig:.2f}")
#    elif choice == 3:
#       orig = float(input("Original: $"))
#       sale = float(input("Sale: $"))
#       pct = (1 - sale/orig) * 100
#       print(f"Discount: {pct:.2f}%")

# HINT: pct/100 converts 20% → 0.20
# HINT: 1 - 0.20 = 0.80 (pay 80% of original)

# EXPECTED OUTPUT:
# 1) Sale Price  2) Original Price  3) Discount %
# Choose: 2
# Sale: $80
# Discount %: 20
# Original: $100.00

# EXTENSION CHALLENGES:
# - Stackable discounts (10% then 5% = 14.5% total, not 15%)
# - Tax calculation after discount
# - Buy X get Y free equivalent discount %

print("=== Discount Calculator ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")