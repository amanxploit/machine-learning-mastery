"""
Exercise 2: Personal Finance Calculator
========================================
Calculate compound interest, loan payments, investment growth, savings goals.

CONCEPTS USED (Days 1-5):
- Variables, types, casting
- Arithmetic operators (+, -, *, /, **)
- math.pow() or ** for exponents
- round() for currency
- if/elif/else
- Percentages as decimals (5% = 0.05)
- Functions

REQUIREMENTS:
4 Calculators in menu:
1. COMPOUND INTEREST
   Inputs: Principal, Annual Rate %, Years, Compounds/year (1,4,12,365)
   Formula: A = P(1 + r/n)^(nt)
   Output: Final Amount, Interest Earned

2. LOAN PAYMENT (Mortgage/Auto/Student)
   Inputs: Loan Amount, Annual Rate %, Years
   Formula: P = L × [r(1+r)^n] / [(1+r)^n - 1]
   where r = monthly rate (annual/12/100), n = months
   Output: Monthly Payment, Total Paid, Total Interest

3. INVESTMENT GROWTH (with monthly contributions)
   Inputs: Initial Investment, Monthly Contribution, Annual Return %, Years
   Formula: FV = P(1+r)^n + PMT × [((1+r)^n - 1)/r] × (1+r)
   Output: Future Value, Total Contributed, Total Gains

4. SAVINGS GOAL (time to reach target)
   Inputs: Target Amount, Current Savings, Monthly Savings, Annual Return %
   Output: Months/Years to reach goal

EXAMPLE OUTPUT:
```
=== PERSONAL FINANCE CALCULATOR ===
1. Compound Interest
2. Loan Payment
3. Investment Growth
4. Savings Goal
0. Exit
Choice: 2

--- Loan Payment ---
Loan Amount: $200000
Annual Rate %: 6.5
Years: 30

Monthly Payment: $1,264.14
Total Paid: $455,090.40
Total Interest: $255,090.40
```

TODO: Implement below
"""

import math

# TODO: Implement formula functions
def compound_interest(principal, annual_rate_pct, years, compounds_per_year):
    """Return (final_amount, interest_earned)"""
    pass

def loan_payment(principal, annual_rate_pct, years):
    """Return (monthly_payment, total_paid, total_interest)"""
    pass

def investment_growth(initial, monthly, annual_return_pct, years):
    """Return (future_value, total_contributed, gains)"""
    pass

def savings_goal(target, current, monthly, annual_return_pct):
    """Return months to reach goal (or None if impossible)"""
    pass

def format_money(amount):
    """Format as $X,XXX.XX"""
    pass

# TODO: Menu functions for each calculator
def menu_compound_interest():
    pass

def menu_loan_payment():
    pass

def menu_investment_growth():
    pass

def menu_savings_goal():
    pass

def main():
    print("=== PERSONAL FINANCE CALCULATOR ===")
    # Your menu loop here

if __name__ == "__main__":
    main()