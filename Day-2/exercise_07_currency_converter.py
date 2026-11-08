# Exercise 7: Currency Converter
# ==============================
# REAL-LIFE SCENARIO: Travel apps, e-commerce, forex trading
# WHY THIS MATTERS: Multiplication by exchange rate — same math as
#                   feature scaling (multiply by factor), normalization

# LEARNING OBJECTIVES:
# - Multiplication for unit conversion
# - Dictionary-like thinking (rate lookup)
# - Precision with financial calculations

# YOUR TASK:
# 1. Define exchange rates (hardcoded): USD to EUR, GBP, JPY, INR
# 2. Ask for USD amount (float)
# 3. Ask for target currency code (EUR/GBP/JPY/INR)
# 4. Convert and print result

# RATES (approximate, use these):
# 1 USD = 0.92 EUR
# 1 USD = 0.79 GBP
# 1 USD = 150.00 JPY
# 1 USD = 83.00 INR

# STEP-BY-STEP:
# 1. rates = {"EUR": 0.92, "GBP": 0.79, "JPY": 150.00, "INR": 83.00}
# 2. usd = float(input("Amount in USD: $"))
# 3. target = input("Convert to (EUR/GBP/JPY/INR): ").upper()
# 4. if target in rates:
#       result = usd * rates[target]
#       print(f"${usd:.2f} = {result:.2f} {target}")
#    else:
#       print("Unknown currency")

# HINT: .upper() handles 'eur' → 'EUR'
# HINT: Dictionary lookup: rates["EUR"] returns 0.92

# EXPECTED OUTPUT:
# Amount in USD: 100
# Convert to (EUR/GBP/JPY/INR): EUR
# $100.00 = 92.00 EUR

# EXTENSION CHALLENGES:
# - Add inverse conversion (foreign → USD)
# - Fetch live rates from API (later!)
# - Handle multiple conversions in one run

print("=== Currency Converter ===")
# YOUR CODE BELOW THIS LINE

rates = {"EUR": 0.92, "GBP": 0.79, "JPY": 150.00, "INR": 83.00}
usd = float(input("Amount in USD: $"))
target = input("Convert to (EUR/GBP/JPY/INR): ").upper()

if target in rates:
    result = usd * rates[target]
    print(f"${usd:.2f} = {result:.2f} {target}")
else:
    print("Unknown currency")

# YOUR CODE ABOVE THIS LINE
print("=== Done ===")