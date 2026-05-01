class BankAccount:
    def __init__(self, number: int, name: str, balance: float = 0):
        self.number = number
        self.name = name
        self.__balance = balance

    def _validate_amount(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")

    def deposit(self, amount: float):
        self._validate_amount(amount)
        self.__balance += amount

    def withdraw(self, amount: float):
        self._validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def transfer(self, amount: float, other_account: "BankAccount"):
        self._validate_amount(amount)
        self.withdraw(amount)
        other_account.deposit(amount)

    def get_account_info(self):
        print(f'{self.name}-{self.number} has {self.__balance}')
