# Напишите определение классов Transport Car Boat и Plane

class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue, kind="Car"):
        super().__init__(brand, max_speed, kind)
        self.__gasoline_residue = gasoline_residue
        self.mileage = mileage

    @property
    def gasoline(self):
        return f"Осталось бензина {self.__gasoline_residue} л"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f"Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л")
        else:
            print("Ошибка заправки автомобиля")


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name, kind="Boat"):
        super().__init__(brand, max_speed, kind)
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind="Plane")
        self.capacity = capacity

    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"


# Ниже располагается код для проверки

p1 = Transport('Chuck', 50)
print(p1)
assert isinstance(p1, Transport)
assert p1.kind == None
assert p1.brand == 'Chuck'
assert p1.max_speed == 50
assert p1.__dict__ == {'kind': None, 'brand': 'Chuck', 'max_speed': 50}

c1 = Car('RRR', 50, 150, 999)
print(c1)

assert isinstance(c1, Car)
assert c1.kind == "Car"
assert c1.brand == 'RRR'
assert c1.max_speed == 50
assert c1.mileage == 150
assert c1.gasoline == 'Осталось бензина 999 л'
c1.gasoline = 100
assert c1.gasoline == 'Осталось бензина 1099 л'
assert c1.__dict__ == {'kind': 'Car', 'brand': 'RRR', 'max_speed': 50,
                       'mileage': 150, '_Car__gasoline_residue': 1099}

b1 = Boat('XXX', 1150, 'Arkasha')
print(b1)
assert isinstance(b1, Boat)
assert b1.kind == "Boat"
assert b1.brand == 'XXX'
assert b1.max_speed == 1150
assert b1.owners_name == 'Arkasha'

pla = Plane('www', 2150, 777)
print(pla)
assert isinstance(pla, Plane)
assert pla.kind == "Plane"
assert pla.brand == 'www'
assert pla.max_speed == 2150
assert pla.capacity == 777

transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic может вмещать в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Автомобиль успешно заправлен'
print(first_car.gasoline)  # Осталось бензина на 350 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr
