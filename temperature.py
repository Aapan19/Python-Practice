# Temperature Conversion

unit = input("What is the unit? (C/F): ")
temp = float(input("Enter the Temperature: "))


if unit == "C":
    temp = round(((9*temp)/5) + 32, 2)
    print(f"Your temperature is {temp}°F ")
elif unit == "F":
    temp = round((temp-32)*(5/9), 2)
    print(f"Your temperature is {temp}°C ")
else:
    print(f"{unit} is Invalid")
