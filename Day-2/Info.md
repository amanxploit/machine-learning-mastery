# Day 2: Python Fundamentals — Variables, Data Types & User Input

## 🎯 Learning Objectives
- Understand variables as containers for values
- Learn Python's core data types: `str`, `int`, `float`, `bool`
- Master f-strings for formatted output
- Practice type casting between data types
- Use `input()` for interactive programs
- Build two practical mini-projects

---

## 📦 Core Concepts Covered

### 1. Variables & Data Types

| Type | Keyword | Example | Description |
|------|---------|---------|-------------|
| **String** | `str` | `"Aman Bhagat"` | Text data, enclosed in quotes |
| **Integer** | `int` | `16` | Whole numbers (positive/negative) |
| **Float** | `float` | `10.99` | Decimal numbers |
| **Boolean** | `bool` | `True` / `False` | Logical values |

```python
# Variable assignment
first_name = "Aman Bhagat"   # str
age = 16                      # int
price = 10.99                 # float
is_student = True             # bool
```

**Key insight:** Variables behave *as if they were the value they contain*.

---

### 2. f-Strings (Formatted String Literals)

```python
print(f"Your Name is: {first_name}")
# Output: Your Name is: Aman Bhagat

print(f"The price is: ${price}.")
# Output: The price is: $10.99.
```

**Syntax:** `f"text {variable} text"` — embed expressions directly in strings.

---

### 3. The `type()` Function

```python
print(type(first_name))  # <class 'str'>
print(type(age))         # <class 'int'>
print(type(price))       # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

Essential for debugging and understanding what type a variable holds.

---

### 4. Type Casting (Type Conversion)

| Conversion | Function | Example | Result |
|------------|----------|---------|--------|
| **int → str** | `str()` | `str(16)` | `"16"` |
| **float → int** | `int()` | `int(8.9)` | `8` (truncates!) |
| **str → bool** | `bool()` | `bool("hello")` | `True` |
| **empty → bool** | `bool()` | `bool("")` | `False` |

```python
age = 16
age = str(age)        # "16" (string)
print(type(age))      # <class 'str'>

gpa = 8.9
gpa = int(gpa)        # 8 (integer, decimal truncated)
print(type(gpa))      # <class 'int'>

name = "Aman"
name = bool(name)     # True (non-empty string)
```

**⚠️ Gotcha:** `int(8.9)` → `8` (not `9`) — it truncates, doesn't round!

---

### 5. User Input with `input()`

```python
name = input("What is your name?: ")           # Returns str
age = int(input("What is your age?: "))        # Convert to int immediately

age = age + 1                                  # Arithmetic
print(f"Hello, {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")
```

**Key points:**
- `input()` **always returns a string** — cast explicitly if needed
- Chain casting: `int(input(...))` for numeric input
- Use `float(input(...))` for decimal input

---

### 6. Arithmetic Operations

```python
# Rectangle area
length = float(input("Enter the length?: "))
width = float(input("Enter the width?: "))
area = length * width

# Shopping cart total
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
```

---

## 🛠️ Practical Exercises

### Exercise 1: Rectangle Area Calculator (`Exercise1.py`)

```python
# Exercise 1 Rectangle Area Calc
length = float(input("Enter the length?: "))
width = float(input("Enter the width?: "))
area = length * width

print(f"The area is: {area}cm")
```

**Concepts applied:** `input()`, `float()`, multiplication, f-strings

---

### Exercise 2: Shopping Cart Program (`Exercise2.py`)

```python
# Exercise 2 Shopping Cart Program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"The Total price is ${total}.")
```

**Concepts applied:** `input()`, `float()`, `int()`, multiplication, f-strings, multiple variables

---

## 📚 Key Takeaways

| Concept | Why It Matters for ML |
|---------|----------------------|
| **Variables** | Store data, features, labels, hyperparameters |
| **Data types** | NumPy arrays require specific dtypes (`float32`, `int64`) |
| **Type casting** | Data preprocessing — convert raw input to numeric arrays |
| **`input()`** | Interactive scripts, CLI tools, data collection |
| **Arithmetic** | Foundation for loss functions, gradients, matrix ops |
| **f-strings** | Logging, debugging, formatted output for reports |

---

## ✅ Day 2 Checklist

- [x] Variables and 4 core data types understood
- [x] f-strings for formatted output
- [x] `type()` for inspection
- [x] Type casting: `str()`, `int()`, `float()`, `bool()`
- [x] `input()` with proper casting
- [x] Arithmetic operations (`+`, `*`, etc.)
- [x] Exercise 1: Rectangle Area Calculator
- [x] Exercise 2: Shopping Cart Program
- [x] This documentation created

---

## 🎯 Next Steps (Day 3 Preview)
- Control flow: `if`, `elif`, `else`
- Comparison & logical operators
- Loops: `for`, `while`
- Lists and basic data structures
- Functions (`def`)

---

## 📝 Reflection

> **Time spent:** ~3 hours  
> **Biggest win:** Built two interactive programs from scratch  
> **Challenge:** Remembering `input()` returns string — forgot to cast at first  
> **Insight:** Type casting is everywhere in ML — CSV strings → numeric arrays → tensors  
> **Mindset:** "Every complex ML pipeline starts with basic variable manipulation."

---

*Last updated: 2026-11-06*  
*Part of: [Machine Learning Mastery Journey](../README.md)*