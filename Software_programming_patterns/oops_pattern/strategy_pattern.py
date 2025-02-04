from abc import ABC, abstractmethod
from typing import List

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, expiry: str):
        self.card_number = card_number
        self.expiry = expiry
    
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using Credit Card ending with {self.card_number[-4:]}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using PayPal account: {self.email}")

class BankTransferPayment(PaymentStrategy):
    def __init__(self, bank_account: str):
        self.bank_account = bank_account
    
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using Bank Transfer from account: {self.bank_account}")

# Context
class ShoppingCart:
    def __init__(self):
        self.items: List[float] = []
        self.payment_strategy: PaymentStrategy = None
    
    def add_item(self, price: float) -> None:
        self.items.append(price)
    
    def set_payment_strategy(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy = payment_strategy
    
    def checkout(self) -> None:
        total = sum(self.items)
        if self.payment_strategy:
            self.payment_strategy.pay(total)
        else:
            raise Exception("Please set a payment strategy")

# Example usage
if __name__ == "__main__":
    # Create shopping cart
    cart = ShoppingCart()
    
    # Add items
    cart.add_item(100)
    cart.add_item(50)
    
    # Pay with credit card
    cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456", "12/24"))
    cart.checkout()
    
    # Create new cart
    cart = ShoppingCart()
    cart.add_item(75)
    
    # Pay with PayPal
    cart.set_payment_strategy(PayPalPayment("user@example.com"))
    cart.checkout() 