# Exercise 13: Unit Converter (Length)
# ====================================
# REAL-LIFE SCENARIO: Engineering, construction, international trade
# WHY THIS MATTERS: Feature scaling — converting all features to same unit
#                   before feeding to ML model (critical for distance-based algos)

# LEARNING OBJECTIVES:
# - Conversion factors as multiplication
# - Chain conversions (mm → m → km)
# - Organizing related constants

# CONVERSIONS (base = meter):
# 1 km = 1000 m
# 1 m = 100 cm
# 1 m = 1000 mm
# 1 in = 2.54 cm
# 1 ft = 12 in
# 1 yd = 3 ft
# 1 mi = 5280 ft

# YOUR TASK:
# 1. Define all factors relative to METER
# 2. Ask value, from_unit, to_unit
# 3. Convert: value × (from_factor / to_factor)
# 4. Support: km, m, cm, mm, in, ft, yd, mi

# STEP-BY-STEP:
# 1. to_meter = {"km": 1000, "m": 1, "cm": 0.01, "mm": 0.001,
#                "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34}
# 2. val = float(input("Value: "))
# 3. from_u = input("From (km/m/cm/mm/in/ft/yd/mi): ")
# 4. to_u = input("To (km/m/cm/mm/in/ft/yd/mi): ")
# 5. result = val * (to_meter[from_u] / to_meter[to_u])
# 6. print(f"{val} {from_u} = {result:.4f} {to_u}")

# HINT: Convert to meters first, then to target: val * from_factor / to_factor
# HINT: .4f for precision (small units like mm)

# EXPECTED OUTPUT:
# Value: 1
# From: mi
# To: km
# 1 mi = 1.6093 km

# Value: 100
# From: cm
# To: in
# 100 cm = 39.3701 in

# EXTENSION CHALLENGES:
# - Add weight (kg, g, lb, oz) and volume (L, mL, gal) converters
# - Temperature (needs formula, not just factor)
# - Pretty table of all conversions for given value

print("=== Length Unit Converter ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")