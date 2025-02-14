# Exercise. BankAccount class with the following features:
# Attributes:
# account_holder (name of the account holder)
# balance (default to 0)
# Methods:
# deposit(amount): Adds money to the balance.
# withdraw(amount): Deducts money from the balance if sufficient funds are available; otherwise, print an error.
# get_balance(): Returns the current balance.
# __str__(): Returns a string representation of the account details.

class BankAccount:
    def __init__(self, account_holder, balance = 0): # balance default to 0
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}. Balance: $ {self.balance:.2f}"
    
    def get_balance(self):
        return self.balance
    
    def print_balance(self):
        print(f"Your balance is: $ {self.get_balance():.2f}\n")

    def deposit(self, amount_to_add):
        if amount_to_add <= 0:
            print(f"Cannot add value to balance: {amount_to_add}. Deposit amount must be positive\n")
            return
        self.balance += amount_to_add
        print(f"${amount_to_add:.2f} were added to your balance.")
        self.print_balance()
    
    def withdraw(self, amount_to_withdraw):
        # print(amount_to_withdraw)
        # print(self.get_balance())
        if amount_to_withdraw <= 0:
            print(f"Cannot withdraw value: {amount_to_withdraw}. Amount to withdraw must be positive.\n")
            return
        if self.get_balance() >= amount_to_withdraw:
            self.balance -= amount_to_withdraw
            print(f"${amount_to_withdraw:.2f} were withdrawn from your account.")
            self.print_balance()
        else:
            print("Not enough balance to withdraw.")
            self.print_balance()


# testing the class
account = BankAccount("John Doe", 100)
account.deposit(50) # 150
account.withdraw(150)
account.withdraw(20)
account.withdraw(-30)
account.deposit(650) # 150
