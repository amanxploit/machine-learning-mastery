# Day 4: Control Flow — Conditionals & Boolean Logic

## 🎯 Learning Objectives
- Master `if`, `elif`, `else` for decision making
- Use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Apply logical operators (`and`, `or`, `not`)
- Understand truthy/falsy values
- Build interactive programs with input validation

---

## 📦 Core Concepts Covered

### 1. Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |

**Key:** `=` is assignment, `==` is comparison!

---

### 2. Conditional Statements

```python
# Basic if
if age >= 18:
    print("Adult")

# if-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if-elif-else chain
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Multiple conditions
if age >= 18 and has_id:
    print("Can vote")
if age < 18 or not has_permission:
    print("Needs guardian")
```

---

### 3. Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Both must be True | `True and False` → `False` |
| `or` | At least one True | `True or False` → `True` |
| `not` | Negates | `not True` → `False` |

**Short-circuit evaluation:** `and` stops at first `False`; `or` stops at first `True`.

---

### 4. Truthy & Falsy Values

```python
# Falsy (evaluates to False in conditions)
False, None, 0, 0.0, "", [], {}, set()

# Truthy (evaluates to True)
True, 1, 3.14, "hello", [1, 2], {"a": 1}
```

```python
name = input("Enter your name: ")

if name:           # Empty string "" is falsy
    print(f"Hey {name}")
else:
    print("You did not type in your name!")
```

---

## 🛠️ Practical Exercises

### Exercise 1: Simple Calculator (`Exercise1.py`)

```python
operator = input("Enter your operator (+,-,/,*): ")

num1 = float(input("Enter Your 1st Number: "))
num2 = float(input("Enter Your 2nd Number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
else:
    print(f"{operator} is not valid")
```

**Concepts:** `if/elif/else` chain, string comparison, division by zero risk (later fix)

---

### Main Practice: Age Validation (`main.py`)

```python
# Commented example — age check with multiple conditions
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are now signed up!")
# elif age <= 0:
#     print("You haven't been born yet!")
# elif age >= 100:
#     print("You are too old to sign up")
# else:
#     print("You must be 18+ to sign up")

# Active: Name validation using truthy/falsy
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hey {name}")
```

**Concepts:** `elif` chain ordering matters, empty string check

---

## 📚 Key Takeaways

| Concept | Why It Matters for ML |
|---------|----------------------|
| **`if/elif/else`** | Decision trees, rule-based systems, thresholds |
| **Comparison ops** | Feature thresholds, binary classification, ReLU |
| **Logical ops** | Compound conditions, feature gates, attention masks |
| **Truthy/Falsy** | Input validation, default parameters, empty checks |
| **Short-circuit** | Efficiency in large condition chains |

---

## ✅ Day 4 Checklist

- [x] Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- [x] `if`, `elif`, `else` structure
- [x] Logical operators (`and`, `or`, `not`)
- [x] Truthy vs Falsy values
- [x] Empty string validation pattern
- [x] Exercise 1: Operator-based calculator
- [x] This documentation created

---

## 🎯 Next Steps (Day 5 Preview)
- Loops: `for`, `while`
- `range()` and iteration
- Loop control: `break`, `continue`
- List basics (preview)
- Nested loops

---

## 📝 Reflection

> **Time spent:** ~2 hours  
> **Biggest win:** Built a working calculator with operator selection  
> **Challenge:** Remembering `==` vs `=` — classic bug!  
> **Insight:** Conditionals are everywhere in ML — decision boundaries, activation functions, early stopping  
> **Mindset:** "Code that makes decisions is code that *does* something."

---

*Last updated: 2026-11-12*  
*Part of: [Machine Learning Mastery Journey](../README.md)*