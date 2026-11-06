# Exercise 9: Rectangle & Box Properties
# ======================================
# REAL-LIFE SCENARIO: Construction, packaging, UI layout, computer vision
# WHY THIS MATTERS: Bounding boxes in object detection (YOLO, etc.),
#                   feature maps, anchor boxes — all rectangles

# LEARNING OBJECTIVES:
# - Multiple calculations from 2-3 inputs
# - Perimeter vs Area distinction
# - 2D → 3D extension

# FORMULAS:
# Rectangle (length L, width W):
#   Area = L × W,  Perimeter = 2(L + W)
# Box (length L, width W, height H):
#   Volume = L × W × H,  Surface Area = 2(LW + LH + WH)

# YOUR TASK:
# 1. Ask for length, width (float)
# 2. Calculate rectangle area & perimeter
# 3. Ask for height (float)
# 4. Calculate box volume & surface area
# 5. Print all with 2 decimals

# STEP-BY-STEP:
# 1. l = float(input("Length: "))
# 2. w = float(input("Width: "))
# 3. rect_area = l * w
# 4. rect_perim = 2 * (l + w)
# 4. h = float(input("Height: "))
# 5. volume = l * w * h
# 6. surface = 2 * (l*w + l*h + w*h)
# 7. Print formatted results

# HINT: Order of operations — parentheses in 2*(l*w + l*h + w*h) matter!
# HINT: All units consistent (e.g., all cm → cm², cm³)

# EXPECTED OUTPUT:
# Length: 10
# Width: 5
# Height: 4
# Rectangle: Area=50.00, Perimeter=30.00
# Box: Volume=200.00, Surface Area=220.00

# EXTENSION CHALLENGES:
# - Calculate diagonal: sqrt(l² + w²) and sqrt(l² + w² + h²)
# - Given volume and 2 dims, find 3rd dim
# - Packing: how many small boxes fit in large box

print("=== Rectangle & Box Calculator ===")
# YOUR CODE BELOW THIS LINE



# YOUR CODE ABOVE THIS LINE
print("=== Done ===")