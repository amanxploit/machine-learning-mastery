# Day 3: Python Math Module & Built-in Functions

## 🎯 Learning Objectives
- Use the `math` module for advanced mathematical operations
- Apply `math.pi`, `math.sqrt()`, `pow()`, `round()`
- Practice arithmetic operators and augmented assignment
- Build geometry calculators (circle, right triangle)

---

## 📦 Core Concepts Covered

### 1. The `math` Module

```python
import math

math.pi        # 3.141592653589793
math.sqrt(x)   # Square root
pow(x, y)      # x raised to power y (x ** y)
round(x, n)    # Round to n decimal places
```

**Why import?** `math` provides constants (`pi`, `e`) and functions not in built-ins.

---

### 2. Arithmetic Operators Review

| Operator | Example | Result | Augmented |
|----------|---------|--------|-----------|
| `+` | `5 + 3` | 8 | `+=` |
| `-` | `5 - 3` | 2 | `-=` |
| `*` | `5 * 3` | 15 | `*=` |
| `/` | `5 / 3` | 1.666... | `/=` |
| `%` | `5 % 3` | 2 | `%=` |
| `**` | `5 ** 3` | 125 | `**=` |

```python
friends = 4
friends += 1   # 5 (same as friends = friends + 1)
friends *= 2   # 10
friends **= 2  # 100
```

---

### 3. Built-in Math Functions

```python
round(3.14159, 2)    # 3.14
abs(-5)              # 5
max(1, 5, 3)         # 5
min(1, 5, 3)         # 1
pow(2, 3)            # 8 (same as 2 ** 3)
```

---

## 🛠️ Practical Exercises

### Exercise 1: Circle Circumference (`Exercise1.py`)

```python
import math

radius = float(input("Enter the radius of Circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")
```

**Concepts:** `math.pi`, formula `C = 2πr`, `round()`

---

### Exercise 2: Circle Area (`Exercise2.py`)

```python
import math

radius = float(input("Enter the Radius: "))

Area = math.pi * pow(radius, 2)

print(f"The Area is: {round(Area, 2)}")
```

**Concepts:** `math.pi`, `pow(r, 2)` or `r ** 2`, formula `A = πr²`

---

### Exercise 3: Right Triangle Hypotenuse (`Exercise3.py`)

```python
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

r = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side r: {r}")
```

**Concepts:** Pythagorean theorem `c = √(a² + b²)`, `math.sqrt()`, `pow()`

---

## 📚 Key Takeaways

| Concept | Why It Matters for ML |
|---------|----------------------|
| **`math.pi`** | Gaussian distributions, circular statistics, RBF kernels |
| **`math.sqrt()`** | Distance metrics (Euclidean), normalization, RMS |
| **`pow()` / `**`** | Polynomial features, exponential decay, learning curves |
| **`round()`** | Display precision, quantization, discrete outputs |
| **Augmented assignment** | In-place updates (gradient descent: `w -= lr * grad`) |

---

## ✅ Day 3 Checklist

- [x] `import math` and use `math.pi`
- [x] `math.sqrt()` for square roots
- [x] `pow(x, y)` for exponents
- [x] `round(x, n)` for decimal precision
- [x] Arithmetic operators (+, -, *, /, %, **)
- [x] Augmented assignment (+=, -=, *=, /=, **=)
- [x] Exercise 1: Circle circumference
- [x] Exercise 2: Circle area
- [x] Exercise 3: Right triangle hypotenuse
- [x] This documentation created

---

## 🎯 Next Steps (Day 4 Preview)
- Conditional statements: `if`, `elif`, `else`
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical operators (`and`, `or`, `not`)
- Truthy/Falsy values
- Input validation

---

## 📝 Reflection

> **Time spent:** ~2 hours  
> **Biggest win:** Applied math module to real geometry problems  
> **Challenge:** Remembering to `import math` before using `pi` or `sqrt`  
> **Insight:** These math functions are the building blocks of distance calculations in ML (k-NN, clustering, etc.)  
> **Mindset:** "Every complex model starts with basic geometry."

---

*Last updated: 2026-11-12*  
*Part of: [Machine Learning Mastery Journey](../README.md)*