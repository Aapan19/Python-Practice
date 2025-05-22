import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    
    return [random.choice(symbols) for _ in range(3)]
    

def print_now(row):
    print("****************************")
    print("   |   ".join(row))
    print("****************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 7
        elif row[0] == '🔔':
            return bet * 8
        elif row[0] == '⭐':
            return bet * 10
    return 0


def main():
    balance = 100

    print("****************************")
    print("Welcome to Slot Machine Game")
    print("symbols:  🍒 🍉 🍋 🔔 ⭐")
    print("****************************")

    while balance>0:
        print(f"Your current Balance is: ${balance}")
        
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficent funds") 
            continue

        if bet <= 0:
            print("Bet amount must be greater then 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning........\n")
        print_now(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You have won ${payout}")
        else:
            print("Sorry! You have lost the game")

        balance += payout

        play_again = input("Do you want to spin again(Y?N): ").upper()

        if play_again != 'Y':
            break

    print("********************************")
    print(f"Game over! Your Final balance is ${balance}")
    print("********************************")

if __name__ == '__main__':
    main()