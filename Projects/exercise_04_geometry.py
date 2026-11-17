"""
Exercise 4: Geometry Calculator Suite
======================================
2D shapes, 3D shapes, coordinate geometry, triangle solver.

CONCEPTS USED (Days 1-5):
- math module: pi, sqrt, sin, cos, tan, radians, degrees, acos
- Arithmetic operators
- if/elif/else
- Functions
- Loops for menus

REQUIREMENTS:
2D SHAPES (Area, Perimeter):
- Circle: A=πr², C=2πr
- Rectangle: A=w×h, P=2(w+h)
- Square: A=s², P=4s
- Triangle (base/height): A=½bh
- Triangle (3 sides - Heron): A=√(s(s-a)(s-b)(s-c)), s=(a+b+c)/2
- Triangle Solver (3 sides): all angles via Law of Cosines, type classification
- Trapezoid: A=(a+b)h/2
- Regular Polygon: A=ns²/(4tan(π/n)), P=ns

3D SHAPES (Volume, Surface Area):
- Sphere: V=4/3πr³, SA=4πr²
- Cube: V=s³, SA=6s²
- Cylinder: V=πr²h, SA=2πr(r+h)
- Cone: V=⅓πr²h, SA=πr(r+√(r²+h²))
- Rectangular Prism: V=lwh, SA=2(lw+lh+wh)

COORDINATE GEOMETRY:
- 2D Distance: √((x2-x1)² + (y2-y1)²)
- 2D Midpoint: ((x1+x2)/2, (y1+y2)/2)
- 2D Slope: (y2-y1)/(x2-x1) [handle vertical!]
- 3D Distance: √((x2-x1)² + (y2-y1)² + (z2-z1)²)

TRIANGLE SOLVER (3 sides → all properties):
- Validate: a+b>c, a+c>b, b+c>a
- Angles: cos(A)=(b²+c²-a²)/(2bc), etc.
- Type by sides: Equilateral/Isosceles/Scalene
- Type by angles: Right/Acute/Obtuse

EXAMPLE OUTPUT:
```
=== GEOMETRY CALCULATOR SUITE ===
1. 2D Shapes
2. 3D Shapes
3. Coordinate Geometry
0. Exit
Choice: 1

--- 2D SHAPES ---
1. Circle
2. Rectangle
...
5. Triangle Solver (3 sides)
Choice: 5
Side a: 3
Side b: 4
Side c: 5

Area: 6.00
Perimeter: 12.00
Angles: 36.87°, 53.13°, 90.00°
Type: Scalene Right
```

TODO: Implement below
"""

import math

# TODO: 2D shape functions
def circle_area(r): pass
def circle_circumference(r): pass
def rectangle_area(w, h): pass
def rectangle_perimeter(w, h): pass
def triangle_area_heron(a, b, c): pass
def triangle_angles(a, b, c): pass  # return (A, B, C) in degrees
def triangle_type(a, b, c): pass
# ... add more

# TODO: 3D shape functions
def sphere_volume(r): pass
def sphere_surface_area(r): pass
# ... add more

# TODO: Coordinate geometry
def distance_2d(x1, y1, x2, y2): pass
def midpoint_2d(x1, y1, x2, y2): pass
def slope_2d(x1, y1, x2, y2): pass

# TODO: Menu functions
def menu_2d(): pass
def menu_3d(): pass
def menu_coords(): pass

def main():
    print("=== GEOMETRY CALCULATOR SUITE ===")
    # Main menu loop

if __name__ == "__main__":
    main()