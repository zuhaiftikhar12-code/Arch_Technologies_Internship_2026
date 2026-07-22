class ATM:
    def __init__(self):
        self.balance = 0.0

    def show_balance(self):
        print(f"\nYour current balance is: ${self.balance:.2f}")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))

        if amount > 0:
            self.balance += amount
            print("✅ Deposit successful!")
        else:
            print("❌ Invalid amount!")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print("✅ Withdrawal successful!")


class ATMController:
    def __init__(self):
        self.atm = ATM()

    def run(self):
        is_running = True

        while is_running:
            print("\n==============================")
            print("       🏧 ATM Simulation")
            print("==============================")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("==============================")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.atm.show_balance()

            elif choice == "2":
                self.atm.deposit()

            elif choice == "3":
                self.atm.withdraw()

            elif choice == "4":
                print("\n*****************************")
                print(" Thank You! Visit Again 👋")
                print("*****************************")
                is_running = False

            else:
                print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    controller = ATMController()
    controller.run()