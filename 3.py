class BankAccount:
    def __init__(self, number, balance):
        self._account_number = number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

    # Напишите определение класса BankAccount
    class BankAccount:
        def __init__(self, number, balance):
            self._account_number = number
            self._balance = balance

        def get_account_number(self):
            return self._account_number

        def get_balance(self):
            return self._balance

        def set_balance(self, value):
            self._balance = value

        balance = property(fget=get_balance, fset=set_balance)
        account_number = property(fget=get_account_number)

    # Ниже код для проверки методов класса BankAccount
    account = BankAccount("1234567890", 1000)
    assert account._balance == 1000
    assert account._account_number == "1234567890"
    assert account.get_account_number() == "1234567890"
    assert account.get_balance() == 1000
    account.set_balance(1500)
    assert account.get_balance() == 1500

    print('Good')
    balance = property(fget=get_balance, fset=set_balance)
    account_number = property(fget=get_account_number)
