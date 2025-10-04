class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        self._balance = self._balance - amount
        return self._balance

    def print_account_summary(self, account):
        print("Object type : ", type(account),
              " and balance is : ", self.get_balance)


class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        return self._balance * 100 / int(self.interest_rate)


class CheckingAccount(Account):
    def withdraw(self, amount):
        return super().withdraw(amount + 5)


account = SavingsAccount(1000, 10)
option = input("Enter your option : 1) Deposit 2) Withdraw 3) Balance Enquiry")

match option:
    case "2":
        amount = int(input("Enter the amount : "))
        print("You have withdrawn :", amount, " and your new balance is : ", account.withdraw(
            amount) if account.get_balance() > amount else "Your account is not sufficient")
    case "1":
        amount = int(input("Enter the amount : "))
        print("You have deposited :", amount, " and your new balance is : ", account.deposit(
            amount) + account.add_interest())
    case "3":
        print("Your balance is ", account.get_balance() + account.add_interest)
