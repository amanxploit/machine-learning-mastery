"""
Exercise 1: Smart Unit Converter
=================================
Build a menu-driven unit converter with multiple categories.

CONCEPTS USED (Days 1-5):
- Variables, types, casting
- input(), print(), f-strings
- Arithmetic operators
- math module (for π in area)
- if/elif/else chains
- Dictionaries for conversion factors
- while loops (Day 6 preview - try it!)

REQUIREMENTS:
1. Categories: Length, Weight, Temperature, Volume, Area
2. Each category: convert any unit → any other unit
3. Linear conversions (length, weight, volume, area): use base unit factors
4. Temperature: special formulas (C ↔ F, C ↔ K, F ↔ K)
5. Menu-driven interface
6. Input validation (numeric values, valid units)
7. Show formula used
8. Loop until user exits

CONVERSION FACTORS (to base unit):
LENGTH (base: meter)
  km=1000, m=1, cm=0.01, mm=0.001, in=0.0254, ft=0.3048, yd=0.9144, mi=1609.344

WEIGHT (base: gram)
  t=1_000_000, kg=1000, g=1, mg=0.001, lb=453.592, oz=28.3495

VOLUME (base: liter)
  kl=1000, l=1, ml=0.001, gal=3.78541, qt=0.946353, pt=0.473176, cup=0.236588, floz=0.0295735

AREA (base: sq_meter)
  sq_km=1_000_000, sq_m=1, sq_cm=0.0001, sq_mm=0.000001, hectare=10000, acre=4046.86, sq_mi=2_589_988, sq_yd=0.836127, sq_ft=0.092903, sq_in=0.00064516

TEMPERATURE FORMULAS:
  C → F: (C × 9/5) + 32
  C → K: C + 273.15
  F → C: (F - 32) × 5/9
  F → K: (F - 32) × 5/9 + 273.15
  K → C: K - 273.15
  K → F: (K - 273.15) × 9/5 + 32

EXAMPLE OUTPUT:
```
=== SMART UNIT CONVERTER ===
1. Length
2. Weight
3. Temperature
4. Volume
5. Area
0. Exit
Choose (0-5): 1

--- Length Converter ---
Available: km, m, cm, mm, in, ft, yd, mi
From: m
To: ft
Value: 10

Result: 10.00 m = 32.81 ft
Formula: 10 × (1 / 0.3048)
```

TODO: Implement the converter below
"""

import math

# TODO: Define CONVERSIONS dictionary with all categories and units
CONVERSIONS = {
    # Add your conversion factors here
}

# TODO: Implement conversion functions
def convert_general(value, from_unit, to_unit, category):
    """Linear conversion using base unit factors."""
    pass

def convert_temperature(value, from_unit, to_unit):
    """Temperature conversion with formulas."""
    pass

def print_menu():
    """Display main menu."""
    pass

def get_valid_choice(max_choice):
    """Get validated menu choice from user."""
    pass

def get_valid_unit(category):
    """Get validated unit from user."""
    pass

def get_valid_number(prompt):
    """Get validated float from user."""
    pass

# TODO: Main program loop
def main():
    print("=== SMART UNIT CONVERTER ===")
    # Your code here

if __name__ == "__main__":
    main()