# Exercise 8: Circle & Sphere Calculator
# ======================================
# REAL-LIFE SCENARIO: Engineering, physics, graphics, game dev
# WHY THIS MATTERS: π (pi) appears everywhere in ML — Gaussian distributions,
#                   radial basis functions, circular statistics

# LEARNING OBJECTIVES:
# - Use math.pi constant
# - Power operator ** for area/volume
# - Multiple related calculations from one input

# FORMULAS (r = radius):
# Circle:  Area = π × r²,     Circumference = 2 × π × r
# Sphere:  Volume = (4/3) × π × r³,  Surface Area = 4 × π × r²

# YOUR TASK:
# 1. Import math module
# 2. Ask for radius (float)
# 3. Calculate all 4 values
# 4. Print with 2 decimals

# STEP-BY-STEP:
# 1. import math
# 2. r = float(input("Radius: "))
# 3. circle_area = math.pi * r ** 2
# 4. circumference = 2 * math.pi * r
# 5. sphere_volume = (4/3) * math.pi * r ** 3
# 6. sphere_surface = 4 * math.pi * r ** 2
# 7. print(f"Circle: A={circle_area:.2f}, C={circumference:.2f}")
# 8. print(f"Sphere: V={sphere_volume:.2f}, SA={sphere_surface:.2f}")

# HINT: import math gives math.pi (3.14159...)
# HINT: ** 2 = squared, ** 3 = cubed
# HINT: (4/3) is float division in Python 3 — correct!

# EXPECTED OUTPUT:
# Radius: 5
# Circle: A=78.54, C=31.42
# Sphere: V=523.60, SA=314.16

# EXTENSION CHALLENGES:
# - Add cylinder calculations (height input)
# - Calculate radius from given area/volume (inverse)
# - Compare circle vs square area (same perimeter)

print("=== Circle & Sphere Calculator ===")
# YOUR CODE BELOW THIS LINE

import math
r = float(input("Radius: "))
circle_area = math.pi * r ** 2
circumference = 2 * math.pi * r
sphere_volume = (4/3) * math.pi * r ** 3
sphere_surface = 4 * math.pi * r ** 2
print(f"Circle: A={circle_area:.2f}, C={circumference:.2f}")
print(f"Sphere: V={sphere_volume:.2f}, SA={sphere_surface:.2f}")

# YOUR CODE ABOVE THIS LINE
print("=== Done ===")