# Exercise 6: Grade Calculator (Weighted Average)
# ===============================================
# REAL-LIFE SCENARIO: Student portals, LMS, academic reporting
# WHY THIS MATTERS: Weighted averages = dot product — fundamental to
#                   neural networks (weighted sum of inputs), ensemble methods

# LEARNING OBJECTIVES:
# - Weighted average calculation
# - Percentage weights must sum to 100%
# - Multi-component aggregation

# SCENARIO:
# Course grade = (Homework × 20%) + (Midterm × 30%) + (Final × 50%)

# YOUR TASK:
# 1. Ask for 3 scores (0-100 each): homework, midterm, final
# 2. Calculate weighted average
# 3. Assign letter grade:
#    A: ≥90, B: ≥80, C: ≥70, D: ≥60, F: <60
# 4. Print numeric grade (1 decimal) and letter

# STEP-BY-STEP:
# 1. hw = float(input("Homework (0-100): "))
# 2. mid = float(input("Midterm (0-100): "))
# 3. fin = float(input("Final (0-100): "))
# 4. grade = hw*0.20 + mid*0.30 + fin*0.50
# 5. if grade >= 90: letter = 'A'
#    elif grade >= 80: letter = 'B'
#    ... (Day 3 preview!)
# 6. print(f"Grade: {grade:.1f} ({letter})")

# HINT: Weights as decimals: 20% = 0.20, 30% = 0.30, 50% = 0.50
# HINT: Sum of weights = 1.0 (100%)

# EXPECTED OUTPUT:
# Homework (0-100): 85
# Midterm (0-100): 78
# Final (0-100): 92
# Grade: 86.6 (B)

# EXTENSION CHALLENGES:
# - Allow custom weights (must sum to 1.0)
# - Handle extra credit (>100 scores)
# - Calculate minimum final score needed for target grade

print("=== Grade Calculator ===")
# YOUR CODE BELOW THIS LINE

hw = float(input("Homework (0-100): "))
mt = float(input("Midterm (0-100): "))
fin = float(input("Final (0-100): "))

grade = hw * 0.20 + mt * 0.30 + fin * 0.50

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Grade: {grade:.1f} ({letter})")

# YOUR CODE ABOVE THIS LINE
print("=== Done ===")