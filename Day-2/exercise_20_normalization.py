# Exercise 20: Data Normalization (Min-Max Scaling)
# =================================================
# REAL-LIFE SCENARIO: ML preprocessing — StandardScaler, MinMaxScaler
# WHY THIS MATTERS: CRITICAL for ML! Neural nets, k-NN, SVM, K-means
#                   ALL require features on similar scale. This IS the math.

# LEARNING OBJECTIVES:
# - Min-Max Normalization: x' = (x - min) / (max - min) → [0, 1]
# - Z-Score Standardization: x' = (x - mean) / std → mean=0, std=1
# - Inverse transform (denormalization)

# FORMULAS:
# Min-Max:  x_norm = (x - x_min) / (x_max - x_min)
# Z-Score:  x_std = (x - μ) / σ
# Inverse:  x = x_norm × (x_max - x_min) + x_min

# YOUR TASK:
# 1. Ask for 5 data points (simulate a feature column)
# 2. Calculate min, max, mean, std
# 3. Normalize each point (Min-Max → [0,1])
# 4. Standardize each point (Z-Score)
# 5. Print original, normalized, standardized in table

# STEP-BY-STEP:
# 1. Collect 5 numbers: x1, x2, x3, x4, x5
# 2. min_val = min(x1,x2,x3,x4,x5)  # use min() function
# 3. max_val = max(x1,x2,x3,x4,x5)
# 4. mean_val = (x1+x2+x3+x4+x5)/5
# 5. std = sqrt(((x1-mean)²+(x2-mean)²+...)/5)  # population std
#    import math; std = math.sqrt(...)
# 6. For each x:
#       norm = (x - min_val) / (max_val - min_val)
#       std = (x - mean_val) / std_val
# 7. Print table

# HINT: min() and max() work with multiple args: min(1,2,3) = 1
# HINT: std formula — square each deviation, sum, divide by n, sqrt

# EXPECTED OUTPUT:
# Enter 5 values: 10 20 30 40 50
# Original | Min-Max | Z-Score
# 10.00    | 0.00    | -1.41
# 20.00    | 0.25    | -0.71
# 30.00    | 0.50    |  0.00
# 40.00    | 0.75    |  0.71
# 50.00    | 1.00    |  1.41

# EXTENSION CHALLENGES:
# - Robust scaling (median, IQR) for outliers
# - Decimal scaling (divide by 10^j)
# - Apply to new data point using training min/max/mean/std

print("=== Data Normalization ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")