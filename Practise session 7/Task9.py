class BankAccount:
    def __init__(self):
        self.balance = 100000  # Default balance is smaller for simplicity.

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. Balance: {self.balance}")

    def display_balance(self):
        print(f"Balance: {self.balance}")


def main():
    account = BankAccount()

    while True:
        print("\n1. Withdraw")
        print("2. Deposit")
        print("3. Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = int(input("Withdraw amount: "))
            account.withdraw(amount)
        elif choice == "2":
            amount = int(input("Deposit amount: "))
            account.deposit(amount)
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
