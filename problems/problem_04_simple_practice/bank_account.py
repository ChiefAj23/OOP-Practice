# Question 2: Encapsulation Practice
# What is encapsulation in Python?
# >Create a class BankAccount that:
# >Hides the balance (i.e., make it private)
# >Allows depositing money through a method
# >Allows checking the balance through a method
# (No direct access to balance allowed)

class BankAccount:
    def __init__(self, account_number: int, balance: float, owner_name: str):
        self._account_number=account_number
        self._balance=balance
        self._owner_name=owner_name
    @property
    def account_number(self) -> int:
        return self._account_number

    def get_balance(self) -> float:
        return self._balance
    @property
    def owner_name(self) -> str:
        return self._owner_name
    def __str__(self):
        return f"Account: {self._account_number} | Balance: {self._balance} | Owner: {self._owner_name}"

def main():
    b1=BankAccount(123456789,2000,"John Doe")
    return print(b1, "| get_balance:",b1.get_balance())
main()
