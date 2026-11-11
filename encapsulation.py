class BankAccount:
    def __init__(self, balance) -> None:
        self._balance = balance

    def get_balance(self):
        return self.__balance

Bank1 = BankAccount(1000)


print(Bank1._balance)