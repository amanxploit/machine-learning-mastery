"""
Exercise 3: Health & Fitness Tracker
=====================================
Calculate BMI, BMR, TDEE, calorie targets, macros, ideal weight.

CONCEPTS USED (Days 1-5):
- Variables, types, casting
- Arithmetic, math.sqrt(), math.log10()
- if/elif/else chains
- Logical operators (and, or)
- Functions
- File I/O (JSON) for profile save/load

REQUIREMENTS:
User Profile: name, age, gender (M/F), height (cm), weight (kg)

CALCULATIONS:
1. BMI = weight / (height_m)^2
   Categories: <18.5 Underweight, 18.5-25 Normal, 25-30 Overweight, ≥30 Obese

2. BMR (Mifflin-St Jeor):
   Men: 10×W + 6.25×H - 5×A + 5
   Women: 10×W + 6.25×H - 5×A - 161
   (W=kg, H=cm, A=age)

3. TDEE = BMR × Activity Multiplier
   1.2 Sedentary, 1.375 Light, 1.55 Moderate, 1.725 Very Active, 1.9 Extra Active

4. Calorie Targets:
   Maintain = TDEE
   Lose 0.5kg/wk = TDEE - 500
   Gain 0.5kg/wk = TDEE + 500

5. Macro Splits (grams):
   Protein: (cal × %) / 4
   Carbs: (cal × %) / 4
   Fat: (cal × %) / 9
   Presets: Balanced(30/40/30), HighProtein(40/30/30), LowCarb(35/20/45), Keto(20/5/75)

6. Ideal Weight Range (BMI 18.5-24.9)

7. Body Fat % (US Navy Method):
   Men: %BF = 495/(1.0324 - 0.19077×log10(waist-neck) + 0.15456×log10(height)) - 450
   Women: %BF = 495/(1.29579 - 0.35004×log10(waist+hip-neck) + 0.221×log10(height)) - 450

EXAMPLE OUTPUT:
```
=== HEALTH & FITNESS TRACKER ===
Profile: John | 30 | Male | 180cm | 85kg

1. BMI Analysis
2. BMR & TDEE
3. Calorie Targets & Macros
4. Body Fat Estimate
5. Full Report
0. Exit
Choice: 1

--- BMI ANALYSIS ---
BMI: 26.2 ⚠️
Category: Overweight
Ideal Weight: 60.0 - 80.7 kg
```

TODO: Implement below
"""

import math
import json
import os

# TODO: Formula functions
def calculate_bmi(weight_kg, height_m):
    pass

def bmi_category(bmi):
    pass

def calculate_bmr(weight_kg, height_cm, age, gender):
    pass

def calculate_tdee(bmr, activity_level):
    pass

def calorie_targets(tdee, goal):
    pass

def macro_split(calories, preset='balanced'):
    pass

def navy_body_fat_pct(gender, height_cm, neck_cm, waist_cm, hip_cm=None):
    pass

def save_profile(profile):
    pass

def load_profile():
    pass

# TODO: Display functions
def show_bmi(profile):
    pass

def show_bmr_tdee(profile):
    pass

def show_macros(tdee):
    pass

def show_body_fat(profile):
    pass

def main():
    print("=== HEALTH & FITNESS TRACKER ===")
    # Load/create profile, then menu loop

if __name__ == "__main__":
    main()