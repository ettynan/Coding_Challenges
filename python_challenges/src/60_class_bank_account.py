'''Create a class representing a simple bank account with deposit and withdraw methods'''

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}, New Balance: {self.balance}"
        else:
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: {amount}, New Balance: {self.balance}"
        else:
            return "Insufficient balance"

# Example usage
account = BankAccount(100)
print(account.deposit(50))
print(account.withdraw(30))
print(account.withdraw(200))
