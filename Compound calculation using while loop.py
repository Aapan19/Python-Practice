principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle can't be less then o equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate : "))
    if rate <= 0:
        print("Interast rate can't be less then o equal to zero")

while time <= 0:
    time = int(input("Enter the times in years: "))
    if time <= 0:
        print("Time can't be less then o equal to zero")

total = principle * pow((1+(rate/100)), time)

print(f"Your final Balance after {time} years is ${total:.2f}")
