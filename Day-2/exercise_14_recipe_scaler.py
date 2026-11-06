# Exercise 14: Recipe Scaler
# ==========================
# REAL-LIFE SCENARIO: Cooking apps, meal planning, food manufacturing
# WHY THIS MATTERS: Proportional scaling = linear transformation.
#                   Same math as feature scaling, batch normalization!

# LEARNING OBJECTIVES:
# - Ratio calculation: desired_servings / original_servings
# - Multiply all ingredients by same factor
# - Handle fractional ingredients (1.5 cups)

# YOUR TASK:
# 1. Ask original servings (int)
# 2. Ask desired servings (int)
# 3. Ask number of ingredients (int)
# 4. For each ingredient: name, amount, unit
# 5. Scale all amounts, print formatted recipe

# STEP-BY-STEP:
# 1. orig = int(input("Original servings: "))
# 2. desired = int(input("Desired servings: "))
# 3. factor = desired / orig
# 4. n = int(input("Number of ingredients: "))
# 5. Loop n times (Day 3 preview — just copy for now):
#       name = input("Ingredient name: ")
#       amt = float(input("Amount: "))
#       unit = input("Unit: ")
#       scaled = amt * factor
#       print(f"{scaled:.2f} {unit} {name}")

# HINT: factor = desired / orig (e.g., 8/4 = 2.0 for doubling)
# HINT: Loop preview — just repeat the input block n times manually if needed

# EXPECTED OUTPUT:
# Original servings: 4
# Desired servings: 6
# Number of ingredients: 3
# Ingredient name: Flour
# Amount: 2
# Unit: cups
# Ingredient name: Sugar
# Amount: 1
# Unit: cups
# Ingredient name: Eggs
# Amount: 3
# Unit: pieces
# Scaled Recipe (6 servings):
# 3.00 cups Flour
# 1.50 cups Sugar
# 4.50 pieces Eggs

# EXTENSION CHALLENGES:
# - Round to sensible fractions (¼, ⅓, ½ cups)
# - Separate scaling for spices (don't scale linearly!)
# - Nutritional info scaling

print("=== Recipe Scaler ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")