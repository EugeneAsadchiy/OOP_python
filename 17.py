class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if type(i) == int:
                self.values.append(i)
        self.values = sorted(self.values)

    def __str__(self):
        if self.values:
            self.values = sorted(self.values)
            return f"Вектор{tuple(self.values)}"
        else:
            return "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            b = [i + other for i in self.values]
            return Vector(*b)
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                b = [self.values[i] + other.values[i] for i in range(len(self.values))]

                return Vector(*b)
            else:
                print("Сложение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            b = [i * other for i in self.values]
            return Vector(*b)
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                b = [self.values[i] * other.values[i] for i in range(len(self.values))]
                return Vector(*b)
            else:
                print("Умножение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя умножать с {other}")





