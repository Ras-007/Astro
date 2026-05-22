class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def display_details(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)


account = None

while True:
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc_no = input("Enter Account Number: ")
        name = input("Enter Holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        account = BankAccount(acc_no, name, balance)
        print("Account created successfully.")

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))
        account.withdraw(amount)

    elif choice == "4":
        account.check_balance()

    elif choice == "5":
        account.display_details()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
