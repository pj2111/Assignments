class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float):
        # Private attributes (denoted by double underscore)
        self.__account_holder = account_holder
        self.__balance = initial_balance
        
        # Protected attribute (denoted by single underscore)
        self._account_type = "Savings"
    
    # Public methods to access and modify private attributes
    def get_balance(self) -> float:
        return self.__balance
    
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
    
    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount")
    
    # Property decorator - provides controlled access to private attribute
    @property
    def account_holder(self) -> str:
        return self.__account_holder

# Example usage
account = BankAccount("John Doe", 1000)
account.deposit(500)  # Valid
print(account.get_balance())  # Access through method
print(account.account_holder)  # Access through property
# print(account.__balance)  # This would raise an error - private attribute 