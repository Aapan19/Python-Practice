# Shopping card

foods = []
prices = []
total = 0

while true:
    food = input("Enter a food name to bye or Enter q to quit: ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your Total is: $ ")
