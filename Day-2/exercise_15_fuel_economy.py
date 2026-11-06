# Exercise 15: Fuel Economy & Cost
# ================================
# REAL-LIFE SCENARIO: Vehicle tracking, fleet management, trip planning
# WHY THIS MATTERS: Efficiency metrics (distance/fuel) — same as
#                   model efficiency (accuracy/compute), compression ratios

# LEARNING OBJECTIVES:
# - Two common metrics: MPG (US) and L/100km (metric)
# - Cost projection from consumption
# - Unit conversion between systems

# FORMULAS:
# MPG = miles_driven / gallons_used
# L/100km = (liters_used / km_driven) × 100
# Conversion: L/100km = 235.215 / MPG

# YOUR TASK:
# 1. Ask distance (float) and fuel used (float)
# 2. Ask units: "US" (miles/gallons) or "Metric" (km/liters)
# 3. Calculate economy
# 4. Ask fuel price per unit ($/gal or $/L)
# 5. Calculate cost per distance unit

# STEP-BY-STEP:
# 1. dist = float(input("Distance: "))
# 2. fuel = float(input("Fuel used: "))
# 3. system = input("System (US/Metric): ").upper()
# 4. if system == "US":
#       mpg = dist / fuel
#       print(f"Economy: {mpg:.2f} MPG")
#       l_per_100 = 235.215 / mpg
#       print(f"Metric: {l_per_100:.2f} L/100km")
#       price = float(input("Price per gallon: $"))
#       cost_per_mile = price / mpg
#    else:
#       l_per_100 = (fuel / dist) * 100
#       print(f"Economy: {l_per_100:.2f} L/100km")
#       mpg = 235.215 / l_per_100
#       print(f"US: {mpg:.2f} MPG")
#       price = float(input("Price per liter: $"))
#       cost_per_km = price * (l_per_100 / 100)
# 5. Print cost per mile/km

# HINT: 235.215 is exact conversion constant
# HINT: Cost per distance = price / economy

# EXPECTED OUTPUT:
# Distance: 300
# Fuel used: 10
# System (US/Metric): US
# Economy: 30.00 MPG
# Metric: 7.84 L/100km
# Price per gallon: $3.50
# Cost per mile: $0.12

# EXTENSION CHALLENGES:
# - Trip cost calculator (distance × cost_per_unit)
# - CO2 emissions estimate (2.3 kg CO2/L gasoline)
# - Compare vehicles

print("=== Fuel Economy Calculator ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")