# Day 5: Logical Operators & Compound Conditions

## 🎯 Learning Objectives
- Master logical operators: `and`, `or`, `not`
- Combine multiple conditions in `if` statements
- Understand short-circuit evaluation
- Build programs with compound boolean logic

---

## 📦 Core Concepts Covered

### 1. Logical Operators

| Operator | Description | Truth Table |
|----------|-------------|-------------|
| `and` | Both must be True | `True and True` → `True` |
| `or` | At least one True | `True or False` → `True` |
| `not` | Inverts condition | `not True` → `False` |

```python
# and — both conditions required
if temp >= 28 and is_sunny:
    print("Hot outside")

# or — either condition sufficient
if temp > 35 or temp < 0 or is_raining:
    print("Event cancelled")

# not — inversion
if not is_raining:
    print("Enjoy the sunshine!")
```

---

### 2. Short-Circuit Evaluation

```python
# and: stops at first False
result = False and expensive_function()  # expensive_function() never called

# or: stops at first True
result = True or expensive_function()    # expensive_function() never called
```

**Why it matters:** Efficiency, prevents errors (e.g., `x != 0 and 10/x > 5`)

---

### 3. Operator Precedence

```python
# not > and > or
if not a and b or c:
    # Evaluates as: ((not a) and b) or c
    pass
```

**Best practice:** Use parentheses for clarity
```python
if (not a and b) or c:
    pass
```

---

## 🛠️ Practical Exercises

### Main Practice: Weather Conditions (`main.py`)

```python
# Example 1: OR — any bad condition cancels
# temp = 20
# is_raining = False
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# Example 2: AND — both conditions required
temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("it is Hot outside")
elif temp <= 0 and is_sunny:
    print("It is Cold OutSide")
elif temp <= 28 and temp > 0 and is_sunny:
    print("It is Warm OutSide")
```

**Key patterns:**
- `and` for "all must be true" (hot AND sunny)
- `or` for "any triggers" (too hot OR too cold OR raining)
- Range checks: `temp > 0 and temp <= 28`

---

## 📚 Key Takeaways

| Concept | Why It Matters for ML |
|---------|----------------------|
| **`and`** | Feature conjunction, decision tree splits, gating |
| **`or`** | Alternative conditions, ensemble voting, fallback logic |
| **`not`** | Negation, mask inversion, anomaly detection |
| **Short-circuit** | Efficient computation, guards against errors |
| **Compound conditions** | Complex decision boundaries, rule-based systems |

---

## ✅ Day 5 Checklist

- [x] `and` operator — both conditions required
- [x] `or` operator — at least one condition required
- [x] `not` operator — inverts boolean
- [x] Short-circuit evaluation understanding
- [x] Operator precedence (`not` > `and` > `or`)
- [x] Range checks with `and` (`x > 0 and x < 100`)
- [x] Weather condition examples
- [x] This documentation created

---

## 🎯 Next Steps (Day 6 Preview)
- Loops: `for` and `while`
- `range()` function
- Iterating over sequences
- Loop control: `break`, `continue`, `else`
- Nested loops

---

## 📝 Reflection

> **Time spent:** ~1.5 hours  
> **Biggest win:** Understanding how `and`/`or`/`not` combine for complex logic  
> **Challenge:** Remembering precedence — `not` binds tightest!  
> **Insight:** ML models learn these exact logical combinations (decision trees, neural net gates)  
> **Mindset:** "Boolean logic is the skeleton of algorithmic thinking."

---

*Last updated: 2026-11-13*  
*Part of: [Machine Learning Mastery Journey](../README.md)*