# Напишите определение класса QuadraticFunction
class QuadraticFunction:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x, *args, **kwargs):
        y = self.a * (x ** 2) + self.b * x + self.c
        return y


# Ниже код для проверки методов класса QuadraticFunction

f = QuadraticFunction(2, 5, 7)
assert f(1) == 14
assert f(-3) == 10
assert f(2) == 25
assert f(5) == 82

f_2 = QuadraticFunction(-1, 2, 4)
assert f_2(5) == -11
assert f_2(2) == 4
assert f_2(-3) == -11
assert f_2(1) == 5
print('Good')
