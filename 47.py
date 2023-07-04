class Wallet:
    def __init__(self, currency, balance):
        self.balance = balance
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        elif not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        elif self.currency != other.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet):
            raise ValueError(f"Данная операция запрещена")
        elif self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet):
            raise ValueError(f"Данная операция запрещена")
        elif self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance - other.balance)







