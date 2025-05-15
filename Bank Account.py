# Sample Run:
# Deposit: 1000
# Withdraw: 500

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amt):
        self.balance += amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount("John")
acc.deposit(1000)            # Deposited: 1000
acc.withdraw(500)            # Withdrawn: 500
acc.show_balance()           # Balance: 500
