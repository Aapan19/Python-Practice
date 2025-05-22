class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"Fokir! You can withdraw below {self.min_withdraw} tk")
        elif amount > self.max_withdraw:
            print(f"Bank fokir hoye jabe! You can't withdraw more then {self.max_withdraw} tk")
        elif amount > self.balance:
            print(f"Bolod! You have only {self.balance} tk. ")
        else:
            self.balance -= amount
            print(f"Here is your {amount} tk")
            print(f"Your remaing balance is {self.get_balance()} tk")
            print("Thanks for trust on us.")

ibbl = Bank(25000)
ibbl.withdraw(25)
ibbl.withdraw(200000)
ibbl.withdraw(2000)
ibbl.withdraw(24000)
ibbl.deposit(2000)
ibbl.deposit(6000)
print("Your Current balance is", ibbl.get_balance(), "tk")