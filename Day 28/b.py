import random

class BankAccount:
    def __init__(self, account_number, name, initial_balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"💵 Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print(" Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f" Insufficient funds! Current Balance: ${self.balance:.2f}")
        elif amount <= 0:
            print(" Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"💸 Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")

    def display_statement(self):
        print(f"\n--- Account Statement ---")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-------------------------")


class Bank:
    def __init__(self):
        # Stores accounts as {account_number: BankAccount_Object}
        self.accounts = {}

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print(" Initial deposit cannot be negative.")
            return

        # Generate a random 5-digit unique account number
        while True:
            acc_num = str(random.randint(10000, 99999))
            if acc_num not in self.accounts:
                break

        new_account = BankAccount(acc_num, name, initial_deposit)
        self.accounts[acc_num] = new_account
        print(f" Account created successfully for {name}!")
        print(f" Your Account Number is: {acc_num}")

    def get_account(self, acc_num):
        return self.accounts.get(acc_num, None)

    def transfer(self, sender_num, receiver_num, amount):
        sender = self.get_account(sender_num)
        receiver = self.get_account(receiver_num)

        if not sender:
            print(" Sender account not found.")
            return
        if not receiver:
            print(" Receiver account not found.")
            return
        if amount <= 0:
            print(" Transfer amount must be positive.")
            return

        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            print(f" Successfully transferred ${amount:.2f} from {sender.name} to {receiver.name}.")
        else:
            print(f" Transfer failed! Insufficient funds in {sender.name}'s account.")


 
def main():
    bank = Bank()
    
    # Seeding dummy data for instant testing
    bank.create_account("Alice Smith", 500.0)
    bank.create_account("Bob Jones", 200.0)

    while True:
        print("\n======  BANK SYSTEM MENU ======")
        print("1. Open New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance / Statement")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            name = input("Enter Account Holder Name: ")
            try:
                deposit = float(input("Enter Initial Deposit Amount: $"))
                bank.create_account(name, deposit)
            except ValueError:
                print(" Invalid amount. Please enter numbers only.")

        elif choice == "2":
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter amount to deposit: $"))
                    account.deposit(amount)
                except ValueError:
                    print(" Invalid amount.")
            else:
                print(" Account not found.")

        elif choice == "3":
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter amount to withdraw: $"))
                    account.withdraw(amount)
                except ValueError:
                    print(" Invalid amount.")
            else:
                print(" Account not found.")

        elif choice == "4":
            sender = input("Enter YOUR Account Number: ")
            receiver = input("Enter RECEIVER Account Number: ")
            try:
                amount = float(input("Enter amount to transfer: $"))
                bank.transfer(sender, receiver, amount)
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == "5":
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                account.display_statement()
            else:
                print(" Account not found.")

        elif choice == "6":
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()