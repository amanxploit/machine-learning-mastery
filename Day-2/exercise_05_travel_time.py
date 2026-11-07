# Exercise 5: Distance & Travel Time Calculator
# =============================================
# REAL-LIFE SCENARIO: Navigation apps, logistics, trip planning
# WHY THIS MATTERS: Rate × Time = Distance — fundamental physics formula
#                   used in ML for motion prediction, trajectory modeling

# LEARNING OBJECTIVES:
# - Unit consistency (speed in km/h, time in hours)
# - Division for time calculation
# - Hours + minutes formatting

# FORMULAS:
# Distance = Speed × Time
# Time = Distance / Speed

# YOUR TASK:
# 1. Ask for distance in km (float)
# 2. Ask for average speed in km/h (float)
# 3. Calculate time in hours (float)
# 4. Convert to hours + minutes
# 5. Print both formats

# STEP-BY-STEP:
# 1. distance = float(input("Distance (km): "))
# 2. speed = float(input("Speed (km/h): "))
# 3. time_hours = distance / speed
# 4. hours = int(time_hours)
# 5. minutes = (time_hours - hours) * 60
# 6. print(f"Time: {time_hours:.2f} hours = {hours}h {minutes:.0f}m")

# HINT: int() truncates toward zero — gives whole hours
# HINT: (time_hours - hours) gives fractional hours; × 60 = minutes

# EXPECTED OUTPUT:
# Distance (km): 350
# Speed (km/h): 80
# Time: 4.38 hours = 4h 22m

# EXTENSION CHALLENGES:
# - Add break time (e.g., 15 min every 2 hours)
# - Calculate arrival time given departure time
# - Fuel cost: distance × consumption (L/100km) × fuel price

print("=== Distance & Travel Time ===")
# YOUR CODE BELOW THIS LINE

distance = float(input("Distance (km): "))
speed = float(input("Speed (km/h): "))

time_hours = distance / speed
hours = int(time_hours)
minutes = (time_hours - hours) * 60

print(f"Time: {time_hours:.2f} hours = {hours}h {minutes:.0f}m")

# YOUR CODE ABOVE THIS LINE
print("=== Done ===")