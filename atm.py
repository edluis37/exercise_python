class ATM:
    def __init__(self, account_holder, balance=0):
        """Initialize the ATM with an account holder and an initial balance."""
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []  # Track deposits and withdrawals

    def check_balance(self):
        """Display the current balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-" * 30)

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"${amount:.2f} has been deposited into your account.")
        else:
            print("Invalid deposit amount. Must be greater than zero.")
        print("-" * 30)

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Invalid withdrawal amount. Must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds. Cannot withdraw this amount.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"${amount:.2f} has been withdrawn from your account.")
        print("-" * 30)

    def transaction_history(self):
        """Show the transaction history."""
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
        print("-" * 30)




def main():
    # Initialize ATM with a sample account holder and initial balance
    atm = ATM("John Doe", 1000)

    # Main menu for the ATM
    while True:
        print("Welcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        # Get user input
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == '4':
            atm.transaction_history()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
