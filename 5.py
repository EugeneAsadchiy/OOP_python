class Money:
    def __init__(self, dollars, cents):
        # self.dollar = dollars
        # self.cent = cents
        self.total_cents = dollars*100+cents

    @property
    def dollars(self):
        return self.total_cents//100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value*100+self.cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents%100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:

            self.total_cents = self.dollars*100+value
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"

