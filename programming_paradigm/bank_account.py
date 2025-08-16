# bank_account.py

class BankAccount:
    """A simple Bank Account class with deposit, withdraw, and balance display."""

    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are available. Returns True if success else False."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance}")
