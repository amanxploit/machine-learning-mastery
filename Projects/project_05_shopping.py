"""
Project 5: Smart Shopping Assistant
====================================
Cart management, price comparison, budget tracking, discount engine, tax, receipts.
Concepts: all previous + lists, dictionaries, file I/O, loops, functions
"""

import json
import os
from datetime import datetime


# ==================== DATA STRUCTURES ====================
class CartItem:
    """Represents an item in the shopping cart."""
    def __init__(self, name, price, quantity=1, category="General", discount_pct=0):
        self.name = name
        self.price = price           # unit price before discount
        self.quantity = quantity
        self.category = category
        self.discount_pct = discount_pct  # percentage (e.g., 10 for 10%)

    def subtotal(self):
        """Price after discount × quantity."""
        discounted = self.price * (1 - self.discount_pct / 100)
        return discounted * self.quantity

    def savings(self):
        """Total discount amount."""
        return (self.price * self.discount_pct / 100) * self.quantity

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'category': self.category,
            'discount_pct': self.discount_pct
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['price'], d['quantity'], d['category'], d['discount_pct'])


class PriceEntry:
    """Price for an item at a specific store."""
    def __init__(self, item_name, store, price, unit="each"):
        self.item_name = item_name
        self.store = store
        self.price = price
        self.unit = unit


# ==================== CORE SHOPPING FUNCTIONS ====================
def calculate_cart_totals(cart, tax_rate=0):
    """Calculate subtotal, discount, tax, total."""
    subtotal = sum(item.price * item.quantity for item in cart)
    discount = sum(item.savings() for item in cart)
    after_discount = subtotal - discount
    tax = after_discount * tax_rate / 100
    total = after_discount + tax
    return {
        'subtotal': subtotal,
        'discount': discount,
        'after_discount': after_discount,
        'tax': tax,
        'total': total
    }


def apply_coupons(cart, coupons):
    """
    Apply stackable coupons to cart.
    Coupon types: 'pct' (percentage off), 'flat' (fixed $ off), 'bogo' (buy one get one)
    """
    for coupon in coupons:
        if coupon['type'] == 'pct':
            # Percentage off entire cart
            for item in cart:
                item.discount_pct += coupon['value']
        elif coupon['type'] == 'flat':
            # Fixed $ off - distribute proportionally
            total = sum(item.price * item.quantity for item in cart)
            if total > 0:
                for item in cart:
                    item_share = (item.price * item.quantity) / total
                    flat_discount = coupon['value'] * item_share
                    item.discount_pct += (flat_discount / (item.price * item.quantity)) * 100
        elif coupon['type'] == 'bogo':
            # Buy X get Y free - for specific item
            target = coupon.get('item')
            buy = coupon.get('buy', 1)
            get = coupon.get('get', 1)
            for item in cart:
                if item.name.lower() == target.lower():
                    free_qty = (item.quantity // buy) * get
                    item.discount_pct = 100 * free_qty / item.quantity if item.quantity > 0 else 0


def format_money(amount):
    return f"${amount:,.2f}"


def print_receipt(cart, tax_rate=0, store_name="Smart Shop"):
    """Print formatted receipt."""
    totals = calculate_cart_totals(cart, tax_rate)

    width = 50
    print("\n" + "=" * width)
    print(f"{store_name:^50}")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M'):^50}")
    print("=" * width)
    print(f"{'Item':<20} {'Qty':>3} {'Price':>10} {'Disc%':>6} {'Total':>10}")
    print("-" * width)

    for item in cart:
        discounted_price = item.price * (1 - item.discount_pct / 100)
        line_total = discounted_price * item.quantity
        name = item.name[:18] + ".." if len(item.name) > 20 else item.name
        print(f"{name:<20} {item.quantity:>3} {format_money(item.price):>10} "
              f"{item.discount_pct:>5.0f}% {format_money(line_total):>10}")

    print("-" * width)
    print(f"{'Subtotal:':<30} {format_money(totals['subtotal']):>18}")
    if totals['discount'] > 0:
        print(f"{'Discounts:':<30} -{format_money(totals['discount']):>17}")
        print(f"{'After Discount:':<30} {format_money(totals['after_discount']):>18}")
    if tax_rate > 0:
        print(f"{'Tax (' + str(tax_rate) + '%):':<30} {format_money(totals['tax']):>18}")
    print(f"{'TOTAL:':<30} {format_money(totals['total']):>18}")
    print("=" * width)
    print(f"{'Items: ' + str(len(cart)):^50}")
    print("=" * width)


def save_receipt(cart, tax_rate, filename):
    """Save receipt to text file."""
    totals = calculate_cart_totals(cart, tax_rate)
    with open(filename, 'w') as f:
        f.write("=" * 50 + "\n")
        f.write(f"{'Smart Shop Receipt':^50}\n")
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M'):^50}\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'Item':<20} {'Qty':>3} {'Price':>10} {'Disc%':>6} {'Total':>10}\n")
        f.write("-" * 50 + "\n")

        for item in cart:
            discounted_price = item.price * (1 - item.discount_pct / 100)
            line_total = discounted_price * item.quantity
            name = item.name[:18] + ".." if len(item.name) > 20 else item.name
            f.write(f"{name:<20} {item.quantity:>3} {format_money(item.price):>10} "
                   f"{item.discount_pct:>5.0f}% {format_money(line_total):>10}\n")

        f.write("-" * 50 + "\n")
        f.write(f"{'Subtotal:':<30} {format_money(totals['subtotal']):>18}\n")
        if totals['discount'] > 0:
            f.write(f"{'Discounts:':<30} -{format_money(totals['discount']):>17}\n")
            f.write(f"{'After Discount:':<30} {format_money(totals['after_discount']):>18}\n")
        if tax_rate > 0:
            f.write(f"{'Tax (' + str(tax_rate) + '%):':<30} {format_money(totals['tax']):>18}\n")
        f.write(f"{'TOTAL:':<30} {format_money(totals['total']):>18}\n")
        f.write("=" * 50 + "\n")

    print(f"💾 Receipt saved to {filename}")


# ==================== SHOPPING LIST ====================
class ShoppingList:
    """Planned items to buy."""
    def __init__(self):
        self.items = []  # list of dicts: name, qty, category, est_price

    def add(self, name, qty=1, category="General", est_price=0):
        self.items.append({
            'name': name,
            'qty': qty,
            'category': category,
            'est_price': est_price
        })

    def remove(self, name):
        self.items = [i for i in self.items if i['name'].lower() != name.lower()]

    def show(self):
        if not self.items:
            print("  (empty)")
            return
        print(f"{'Item':<20} {'Qty':>3} {'Category':<15} {'Est. Price':>12}")
        print("-" * 55)
        for i in self.items:
            print(f"{i['name']:<20} {i['qty']:>3} {i['category']:<15} "
                  f"{format_money(i['est_price']):>12}")

    def compare_with_cart(self, cart):
        """Show what's in list but not in cart."""
        cart_names = {item.name.lower() for item in cart}
        missing = [i for i in self.items if i['name'].lower() not in cart_names]
        if missing:
            print("\n📋 Items in list but not in cart:")
            for i in missing:
                print(f"  - {i['name']} (qty {i['qty']})")
        else:
            print("\n✅ All list items are in cart!")


# ==================== PRICE COMPARISON ====================
price_db = {}  # item_name -> list of PriceEntry


def add_price(item_name, store, price, unit="each"):
    if item_name not in price_db:
        price_db[item_name] = []
    price_db[item_name].append(PriceEntry(item_name, store, price, unit))


def compare_prices(item_name):
    if item_name not in price_db:
        print(f"No price data for '{item_name}'")
        return

    entries = price_db[item_name]
    print(f"\n💰 Price Comparison: {item_name}")
    print(f"{'Store':<20} {'Price':>10} {'Unit':<10}")
    print("-" * 40)
    for e in sorted(entries, key=lambda x: x.price):
        print(f"{e.store:<20} {format_money(e.price):>10} {e.unit:<10}")

    cheapest = min(entries, key=lambda x: x.price)
    print(f"\n✅ Best deal: {cheapest.store} at {format_money(cheapest.price)}/{cheapest.unit}")


def seed_price_data():
    """Add sample price data."""
    add_price("Milk 1L", "Walmart", 1.29)
    add_price("Milk 1L", "Target", 1.49)
    add_price("Milk 1L", "Costco", 1.19)
    add_price("Bread", "Walmart", 1.99)
    add_price("Bread", "Target", 2.29)
    add_price("Bread", "Local Bakery", 3.50)
    add_price("Eggs 12ct", "Walmart", 2.99)
    add_price("Eggs 12ct", "Target", 3.19)
    add_price("Eggs 12ct", "Costco", 2.49)
    add_price("Chicken Breast 1lb", "Walmart", 3.99)
    add_price("Chicken Breast 1lb", "Target", 4.49)
    add_price("Chicken Breast 1lb", "Butcher", 5.99)


# ==================== INPUT HELPERS ====================
def get_float(prompt, default=None):
    while True:
        try:
            val = input(prompt).strip()
            if not val and default is not None:
                return default
            return float(val)
        except ValueError:
            print("Enter a valid number.")


def get_int(prompt, default=None):
    while True:
        try:
            val = input(prompt).strip()
            if not val and default is not None:
                return default
            return int(val)
        except ValueError:
            print("Enter a valid integer.")


def get_str(prompt, default=None):
    val = input(prompt).strip()
    return val if val else default


# ==================== MENUS ====================
def menu_cart(cart, tax_rate):
    while True:
        print("\n--- CART MANAGEMENT ---")
        print("  1. Add Item")
        print("  2. Remove Item")
        print("  3. Update Quantity")
        print("  4. Apply Discount to Item")
        print("  5. View Cart")
        print("  6. Apply Coupons")
        print("  7. Checkout (Print Receipt)")
        print("  0. Back")

        choice = get_int("Choice (0-7): ")

        if choice == 0:
            break

        if choice == 1:
            name = get_str("Item name: ")
            price = get_float("Price per unit: $")
            qty = get_int("Quantity: ", 1)
            cat = get_str("Category: ", "General")
            disc = get_float("Discount % (0 if none): ", 0)
            cart.append(CartItem(name, price, qty, cat, disc))
            print(f"✅ Added {qty}× {name}")

        elif choice == 2:
            if not cart:
                print("Cart is empty.")
                continue
            for i, item in enumerate(cart):
                print(f"  {i+1}. {item.name} (qty {item.quantity})")
            idx = get_int("Remove item #: ") - 1
            if 0 <= idx < len(cart):
                removed = cart.pop(idx)
                print(f"🗑️ Removed {removed.name}")
            else:
                print("Invalid number.")

        elif choice == 3:
            if not cart:
                print("Cart is empty.")
                continue
            for i, item in enumerate(cart):
                print(f"  {i+1}. {item.name} (qty {item.quantity})")
            idx = get_int("Update item #: ") - 1
            if 0 <= idx < len(cart):
                new_qty = get_int("New quantity: ", 1)
                if new_qty > 0:
                    cart[idx].quantity = new_qty
                    print(f"✅ Updated quantity to {new_qty}")
                else:
                    cart.pop(idx)
                    print("🗑️ Removed (quantity 0)")

        elif choice == 4:
            if not cart:
                print("Cart is empty.")
                continue
            for i, item in enumerate(cart):
                print(f"  {i+1}. {item.name} (disc {item.discount_pct}%)")
            idx = get_int("Item #: ") - 1
            if 0 <= idx < len(cart):
                disc = get_float("New discount %: ", 0)
                cart[idx].discount_pct = max(0, min(100, disc))
                print(f"✅ Discount set to {cart[idx].discount_pct}%")

        elif choice == 5:
            if not cart:
                print("🛒 Cart is empty.")
            else:
                print_receipt(cart, tax_rate)

        elif choice == 6:
            print("Coupon Types:")
            print("  1. Percentage off entire cart (e.g., 10%)")
            print("  2. Flat $ off entire cart (e.g., $5)")
            print("  3. BOGO (Buy X Get Y free on specific item)")
            ctype = get_int("Choose (1-3): ")

            coupons = []
            if ctype == 1:
                pct = get_float("Percentage off: ")
                coupons.append({'type': 'pct', 'value': pct})
            elif ctype == 2:
                flat = get_float("Flat $ off: $")
                coupons.append({'type': 'flat', 'value': flat})
            elif ctype == 3:
                item = get_str("Item name: ")
                buy = get_int("Buy: ", 1)
                get_free = get_int("Get free: ", 1)
                coupons.append({'type': 'bogo', 'item': item, 'buy': buy, 'get': get_free})

            apply_coupons(cart, coupons)
            print("✅ Coupons applied!")

        elif choice == 7:
            if not cart:
                print("Cart is empty.")
                continue
            print_receipt(cart, tax_rate)
            save = input("Save receipt to file? (y/n): ").strip().lower()
            if save == 'y':
                fname = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                save_receipt(cart, tax_rate, fname)

def menu_budget(cart, budget):
    if budget <= 0:
        print("No budget set.")
        return budget

    totals = calculate_cart_totals(cart)
    spent = totals['total']
    remaining = budget - spent

    print(f"\n💰 Budget: {format_money(budget)}")
    print(f"💸 Current Total: {format_money(spent)}")
    print(f"💵 Remaining: {format_money(remaining)}")

    pct = spent / budget * 100
    if pct >= 100:
        print("🔴 OVER BUDGET!")
    elif pct >= 95:
        print("🟡 Warning: 95% of budget used!")
    elif pct >= 80:
        print("🟢 Caution: 80% of budget used.")
    else:
        print("✅ Within budget.")

    return budget


def menu_shopping_list(shopping_list, cart):
    while True:
        print("\n--- SHOPPING LIST ---")
        print("  1. Add to List")
        print("  2. Remove from List")
        print("  3. View List")
        print("  4. Compare with Cart")
        print("  5. Move Item to Cart")
        print("  0. Back")

        choice = get_int("Choice (0-5): ")

        if choice == 0:
            break

        if choice == 1:
            name = get_str("Item name: ")
            qty = get_int("Quantity: ", 1)
            cat = get_str("Category: ", "General")
            price = get_float("Est. price (optional): $", 0)
            shopping_list.add(name, qty, cat, price)
            print(f"📝 Added to list")

        elif choice == 2:
            name = get_str("Item to remove: ")
            shopping_list.remove(name)
            print("🗑️ Removed")

        elif choice == 3:
            shopping_list.show()

        elif choice == 4:
            shopping_list.compare_with_cart(cart)

        elif choice == 5:
            if not shopping_list.items:
                print("List is empty.")
                continue
            for i, item in enumerate(shopping_list.items):
                print(f"  {i+1}. {item['name']} (qty {item['qty']})")
            idx = get_int("Move item #: ") - 1
            if 0 <= idx < len(shopping_list.items):
                item = shopping_list.items.pop(idx)
                cart.append(CartItem(item['name'], item['est_price'], item['qty'], item['category']))
                print(f"🛒 Moved {item['name']} to cart")


def menu_price_compare():
    while True:
        print("\n--- PRICE COMPARISON ---")
        print("  1. Compare Prices for Item")
        print("  2. Add Price Entry")
        print("  3. View All Tracked Items")
        print("  0. Back")

        choice = get_int("Choice (0-3): ")

        if choice == 0:
            break

        if choice == 1:
            name = get_str("Item name: ")
            compare_prices(name)

        elif choice == 2:
            name = get_str("Item name: ")
            store = get_str("Store: ")
            price = get_float("Price: $")
            unit = get_str("Unit (each/lb/oz): ", "each")
            add_price(name, store, price, unit)
            print("✅ Price added")

        elif choice == 3:
            if not price_db:
                print("No items tracked.")
            else:
                for item_name in sorted(price_db.keys()):
                    cheapest = min(price_db[item_name], key=lambda x: x.price)
                    print(f"  {item_name}: best {format_money(cheapest.price)} at {cheapest.store}")


def menu_tax():
    print("\n--- TAX SETTINGS ---")
    print("Common rates: 0% (OR, MT, NH, DE), 4-7% (most states), 8-10% (CA, WA, TN)")
    return get_float("Tax rate %: ", 0)


# ==================== MAIN ====================
def main():
    print("=" * 50)
    print("    SMART SHOPPING ASSISTANT")
    print("=" * 50)

    # Initialize
    cart = []
    shopping_list = ShoppingList()
    tax_rate = 0
    budget = 0
    seed_price_data()

    while True:
        print(f"\n🛒 Cart: {len(cart)} items | 📋 List: {len(shopping_list.items)} items | "
              f"💰 Budget: {format_money(budget) if budget else 'Not set'} | "
              f"📊 Tax: {tax_rate}%")

        print("\nMain Menu:")
        print("  1. Cart Management")
        print("  2. Budget Tracker")
        print("  3. Shopping List")
        print("  4. Price Comparison")
        print("  5. Set Tax Rate")
        print("  6. Set Budget")
        print("  0. Exit")

        choice = get_int("Choice (0-6): ")

        if choice == 0:
            print("\nHappy shopping! 🛍️")
            break
        elif choice == 1:
            menu_cart(cart, tax_rate)
        elif choice == 2:
            budget = menu_budget(cart, budget)
        elif choice == 3:
            menu_shopping_list(shopping_list, cart)
        elif choice == 4:
            menu_price_compare()
        elif choice == 5:
            tax_rate = menu_tax()
        elif choice == 6:
            budget = get_float("Budget: $")
            print(f"💰 Budget set to {format_money(budget)}")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()