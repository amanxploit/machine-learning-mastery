# Exercise 18: Statistics Basics (Mean, Median, Range)
# ===================================================
# REAL-LIFE SCENARIO: Data analysis, quality control, ML preprocessing
# WHY THIS MATTERS: Descriptive statistics — first step in EDA.
#                   Mean = centering, Range/Std = scaling (StandardScaler!)

# LEARNING OBJECTIVES:
# - Mean = sum / count
# - Range = max - min
# - Collecting multiple inputs into variables

# YOUR TASK:
# 1. Ask how many numbers (int, 3-10)
# 2. Ask for each number (float)
# 3. Track: sum, count, min, max
# 4. Calculate mean and range
# 5. Print results

# STEP-BY-STEP (without lists/loops — Day 3!):
# 1. n = int(input("How many numbers (3-10): "))
# 2. Initialize: total = 0, minimum = None, maximum = None
# 3. Repeat n times:
#       num = float(input(f"Number {{i}}: "))
#       total += num
#       if minimum is None or num < minimum: minimum = num
#       if maximum is None or num > maximum: maximum = num
# 4. mean = total / n
# 5. range_val = maximum - minimum
# 6. print(f"Mean: {mean:.2f} | Range: {range_val:.2f} (Min: {minimum}, Max: {maximum})")

# HINT: Use None for initial min/max — first number sets both
# HINT: Manually repeat input block 5-10 times, or preview loops!

# EXPECTED OUTPUT:
# How many numbers (3-10): 5
# Number 1: 10
# Number 2: 25
# Number 3: 15
# Number 4: 30
# Number 5: 20
# Mean: 20.00 | Range: 20.00 (Min: 10, Max: 30)

# EXTENSION CHALLENGES:
# - Add median (sort needed — Day 3+)
# - Add standard deviation
# - Handle outliers (IQR method)

print("=== Basic Statistics ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")