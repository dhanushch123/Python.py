class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        while True:
            usr_inp = input("""Hello, How would you like to proceed?
Choose an option that performs the required transaction
1. Pin generation
2. Deposit
3. Withdraw
4. Balance inquiry
5. Exit
""")
            if usr_inp == "1":
                print("Pin generation")
                self.pin_generation()
            elif usr_inp == "2":
                print("Deposit")
                self.deposit()
            elif usr_inp == "3":
                print("Withdraw")
                self.withdraw()
            elif usr_inp == "4":
                print("Balance inquiry")
                self.show_balance()
            elif usr_inp == "5":
                print("Thank you")
                break
            else:
                print("Enter a valid input")

    def pin_generation(self):
        self.pin = input("Enter a new PIN: ")

    def deposit(self):
        if self.get_pin():
            amount = int(input("Enter the amount to be deposited: "))
            self.balance += amount
            print(f"Deposited {amount} successfully. Your new balance is {self.balance}")
        else:
            print("Enter a valid PIN")

    def withdraw(self):
        if self.get_pin():
            amount = int(input("Enter the amount to be withdrawn: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} successfully. Your new balance is {self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Enter a valid PIN")

    def show_balance(self):
        if self.get_pin():
            print(f"Your current balance is: {self.balance}")
        else:
            print("Incorrect PIN")

    def get_pin(self):
        inp = input("Enter PIN: ")
        return inp == self.pin

# Usage
if __name__ == "__main__":
    sbi = Atm()
    sbi.menu()
