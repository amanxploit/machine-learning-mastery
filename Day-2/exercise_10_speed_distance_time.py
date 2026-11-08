# Exercise 10: Speed, Distance, Time Triangle
# ============================================
# REAL-LIFE SCENARIO: Physics, logistics, sports analytics, robotics
# WHY THIS MATTERS: The "magic triangle" — any 2 known → find the 3rd.
#                   Core concept: solving for unknown variable (like ML optimization!)

# LEARNING OBJECTIVES:
# - Algebraic rearrangement: D = S×T, S = D/T, T = D/S
# - Menu-driven program structure
# - Input validation basics

# YOUR TASK:
# 1. Print menu: "Calculate: 1) Distance  2) Speed  3) Time"
# 2. Get choice (int)
# 3. Based on choice, ask for the 2 known values
# 4. Calculate and print the unknown

# STEP-BY-STEP:
# 1. print("1) Distance (speed × time)")
# 2. print("2) Speed (distance / time)")
# 3. print("3) Time (distance / speed)")
# 4. choice = int(input("Choose (1/2/3): "))
# 5. if choice == 1:
#       s = float(input("Speed: "))
#       t = float(input("Time: "))
#       d = s * t
#       print(f"Distance: {d:.2f}")
#    elif choice == 2:
#       d = float(input("Distance: "))
#       t = float(input("Time: "))
#       s = d / t
#       print(f"Speed: {s:.2f}")
#    elif choice == 3:
#       d = float(input("Distance: "))
#       s = float(input("Speed: "))
#       t = d / s
#       print(f"Time: {t:.2f}")
#    else: print("Invalid")

# HINT: This uses if/elif/else — Day 3 topic! Preview it now.
# HINT: Division by zero check: if t == 0 or s == 0: print("Error")

# EXPECTED OUTPUT:
# 1) Distance (speed × time)
# 2) Speed (distance / time)
# 3) Time (distance / speed)
# Choose (1/2/3): 2
# Distance: 150
# Time: 2
# Speed: 75.00

# EXTENSION CHALLENGES:
# - Add acceleration formulas (v = u + at, s = ut + ½at²)
# - Unit conversion (km/h ↔ m/s)
# - Average speed for multi-segment trips

print("=== Speed/Distance/Time Calculator ===")
# YOUR CODE BELOW THIS LINE

print("1) Distance (speed × time)")
print("2) Speed (distance / time)")
print("3) Time (distance / speed)")
choice = int(input("Choose (1/2/3): "))

if choice == 1:
    speed = float(input("Speed: "))
    time = float(input("Time: "))
    distance = speed * time
    print(f"Distance: {distance:.2f}")
elif choice == 2:
    distance = float(input("Distance: "))
    time = float(input("Time: "))
    speed = distance / time
    print(f"Speed: {speed:.2f}")
elif choice == 3:
    distance = float(input("Distance: "))
    speed = float(input("Speed: "))
    time = distance / speed
    print(f"Time: {time:.2f}")
else:
    print("Invalid")

# YOUR CODE ABOVE THIS LINE
print("=== Done ===")