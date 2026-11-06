# Exercise 19: Projectile Motion (Physics)
# ========================================
# REAL-LIFE SCENARIO: Game physics, ballistics, sports analytics, robotics
# WHY THIS MATTERS: Quadratic trajectories — parabolas appear in ML
#                   (loss curves, activation functions, optimization paths)

# LEARNING OBJECTIVES:
# - Parametric equations: x(t), y(t)
# - Gravity constant g = 9.8 m/s²
# - Breaking velocity into components

# FORMULAS (no air resistance):
# vx = v₀ × cos(θ)    (constant)
# vy = v₀ × sin(θ) - g×t
# x = vx × t
# y = vy₀ × t - ½gt²
# Max height: H = (v₀² × sin²(θ)) / (2g)
# Range: R = (v₀² × sin(2θ)) / g
# Time of flight: T = (2 × v₀ × sin(θ)) / g

# YOUR TASK:
# 1. Import math (for sin, cos, radians)
# 2. Ask initial velocity m/s (float)
# 3. Ask launch angle degrees (float)
# 4. Calculate max height, range, flight time
# 5. Print all with 2 decimals

# STEP-BY-STEP:
# 1. import math
# 2. v0 = float(input("Initial velocity (m/s): "))
# 3. angle_deg = float(input("Launch angle (degrees): "))
# 4. theta = math.radians(angle_deg)  # Convert to radians!
# 5. g = 9.8
# 6. max_h = (v0**2 * math.sin(theta)**2) / (2*g)
# 7. range_ = (v0**2 * math.sin(2*theta)) / g
# 8. time = (2 * v0 * math.sin(theta)) / g
# 9. print(f"Max Height: {max_h:.2f}m | Range: {range_:.2f}m | Time: {time:.2f}s")

# HINT: math.sin/cos need RADIANS — use math.radians()
# HINT: math.sin(theta)**2 = (sin θ)²

# EXPECTED OUTPUT:
# Initial velocity (m/s): 20
# Launch angle (degrees): 45
# Max Height: 10.20m | Range: 40.82m | Time: 2.88s

# EXTENSION CHALLENGES:
# - Position at specific time t
# - Trajectory points for plotting (loop!)
# - With air resistance (differential equation)

print("=== Projectile Motion ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")