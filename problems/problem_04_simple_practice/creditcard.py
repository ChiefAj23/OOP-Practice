# Question 5: Abstraction in OOP
# Imagine you are building a payment processing system.
# You want to support multiple payment types: CreditCard, PayPal, and BankTransfer.
# Q: How would you use abstraction to design a base class PaymentMethod that enforces all payment types to implement a pay(amount) method?

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCard(PaymentMethod):
    def __init__(self,card_number: int, cardholder_name: str, cvv: int, expiry_date: str):
        self.card_number=card_number
        self.cardholder_name=cardholder_name
        self.expiry_date=expiry_date
        self.cvv=cvv

    def pay(self, amount: float):
        return f"Paid ${amount} using Credit Card ending in {str(self.card_number)[-4:]}"

class PayPal(PaymentMethod):
    def __init__(self,paypal_user_id: int):
        self.paypal_user_id=paypal_user_id

    def pay(self, amount:float):
        return f"Paid ${amount} via PayPal (User ID: {self.paypal_user_id})"

class BankTransfer(PaymentMethod):
    def __init__(self, account_name: str, account_number: int, routing_number: int):
        self.account_name=account_name
        self.account_number=account_number
        self.routing_number=routing_number

    def pay(self, amount):
        return f"Paid ${amount} via bank transfer from {self.account_name}"

def main():
    payments = [
        CreditCard(1234567812345678, "John Doe", 123, "12/26"),
        PayPal("john.doe@example.com"),
        BankTransfer("John Doe", 987654321, 111000025)
    ]

    for method in payments:
        print(method.pay(100.0))
main()


