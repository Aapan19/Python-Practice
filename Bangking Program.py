def show_balance(balance):
    print("*********************")
    print(f"Your Balance is ${balance:.2f}")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter an amount to de deposited: "))
    print("*********************")

    if amount <= 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter an amount to be withdraw: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient Funds! ")
        print("*********************")
        return 0
    elif amount <= 0:
        print("*********************")
        print("Amound must be greater then 0 ")
        print("*********************")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print(" Bangking Program       ")
        print("*********************")
        print("1. Show Balance ")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Exit ")
        print("*********************")

        choice = input("Enter Your choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")
    print("*********************")
    print("Thank You! Have a good day")
    print("*********************")

if __name__ == "__main__":
    main()