# Format Specifiers = {Value:flags} format a value based on what flages are inserted.

price1 = 1200.321
price2 = -1500.6953
price3 = 1400.2541

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")