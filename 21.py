# Напишите определение класса City
class City:
    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return not self.name[-1] in "aeiou"


# Ниже код для проверки методов класса City

p1 = City('new york')
assert p1.name == "New York"
assert p1.__str__() == "New York"
assert isinstance(p1, City)
print(p1)
assert bool(p1)

p2 = City('SaN frANCISco')
assert isinstance(p2, City)
assert p2.name == "San Francisco"
print(p2)
assert not bool(p2)

p3 = City('NIZHNY NoVGORod')
assert p3.name == "Nizhny Novgorod"
print(p3)
assert bool(p3)
assert isinstance(p3, City)
