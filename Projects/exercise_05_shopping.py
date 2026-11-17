"""
Exercise 5: Smart Shopping Assistant
=====================================
Cart, budget, shopping list, price comparison, coupons, tax, receipts.

CONCEPTS USED (Days 1-5 + Lists/Dicts preview):
- Lists, Dictionaries
- Classes (optional) or dicts for items
- Loops (while, for)
- Functions
- File I/O (receipt saving)
- datetime for timestamps
- All previous: variables, math, conditionals, logical ops

REQUIREMENTS:
CART MANAGEMENT:
- Add item: name, price, qty, category, discount%
- Remove item
- Update quantity
- Apply discount to item
- View cart with totals

BUDGET TRACKER:
- Set budget
- Show spent, remaining, % used
- Warnings at 80%, 95%, over

SHOPPING LIST:
- Planned items (name, qty, category, est_price)
- Compare with cart (what's missing)
- Move list item → cart

PRICE COMPARISON:
- Store prices per item (item → [{store, price, unit}])
- Show cheapest store
- Add new price entries

COUPONS (stackable):
- % off entire cart
- $ off entire cart
- BOGO (Buy X Get Y free on specific item)

TAX:
- Configurable tax rate %
- Applied after discounts

RECEIPT:
- Itemized with qty, price, discount%, line total
- Subtotal, discounts, tax, total
- Save to text file

EXAMPLE OUTPUT:
```
=== SMART SHOPPING ASSISTANT ===
Cart: 3 items | List: 5 items | Budget: $100.00 | Tax: 8.5%

1. Cart Management
2. Budget Tracker
3. Shopping List
4. Price Comparison
5. Set Tax Rate
6. Set Budget
0. Exit
Choice: 1

--- CART MANAGEMENT ---
1. Add Item
2. Remove Item
3. Update Quantity
4. Apply Discount
5. View Cart
6. Apply Coupons
7. Checkout
Choice: 1
Item: Milk
Price: 3.99
Qty: 2
Category: Dairy
Discount %: 0
✅ Added 2× Milk

--- RECEIPT ---
Smart Shop                    2026-11-17 14:30
Item                    Qty     Price Disc%     Total
Milk                      2    $3.99   0%    $7.98
Bread                     1    $2.49   0%    $2.49
------------------------------
Subtotal:                      $10.47
Tax (8.5%):                     $0.89
TOTAL:                         $11.36
```

TODO: Implement below
"""

import json
from datetime import datetime

# TODO: Data structures
# Cart item: name, price, quantity, category, discount_pct
# Price entry: item_name, store, price, unit
# Shopping list item: name, qty, category, est_price

# TODO: Core functions
def calculate_totals(cart, tax_rate):
    """Return dict: subtotal, discount, after_discount, tax, total"""
    pass

def apply_coupons(cart, coupons):
    """Modify cart items with coupon discounts"""
    pass

def format_money(amount):
    pass

def print_receipt(cart, tax_rate, store_name="Smart Shop"):
    pass

def save_receipt(cart, tax_rate, filename):
    pass

# TODO: Menu functions
def menu_cart(cart, tax_rate):
    pass

def menu_budget(cart, budget):
    pass

def menu_shopping_list(shopping_list, cart):
    pass

def menu_price_compare():
    pass

# TODO: Sample price data
def seed_prices():
    """Add some default price comparisons"""
    pass

def main():
    print("=== SMART SHOPPING ASSISTANT ===")
    cart = []
    shopping_list = []
    price_db = {}  # item_name -> [{store, price, unit}]
    tax_rate = 0
    budget = 0
    seed_prices()
    # Main menu loop

if __name__ == "__main__":
    main()