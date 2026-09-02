class Bankaccount:
    def __init__(self, starting_balance):
        self.balance = starting_balance


    def deposit(self, amount):
        if amount < 0:
            raise ValueError("the amount cannot be negative")
        self.balance = self.balance + amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            raise ValueError("the wihtdraw amount cannot exceed the balance")
        self.balance = self.balance - withdraw_amount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, starting_balance):
        if starting_balance < 0:
            raise ValueError("invalid balance ")
        self._balance = starting_balance








def main():
    balance = float(input("please enter the initial balance : "))
    account = Bankaccount(balance)
    deposit_amount = float(input("how much would you like to deposit : "))
    account.deposit(deposit_amount)
    print(account.balance)   
    withdraw = float(input("please enter the amount to withdraw : "))
    try:
        account.withdraw(withdraw)     
        print(f"the remaining balance is {account.balance}")     
    except ValueError as e:
        print(e)
    




main()