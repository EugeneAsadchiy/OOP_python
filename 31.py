class Square:
    def get_value(self, a):
        return a * a


class Cube(Square):
    def get_value(self, a):
        return a * a * a


class Power4(Square):
    def get_value(self, a):
        return a ** 4


# Напишите определение классов Cube и Power4

assert issubclass(Cube, Square)
assert issubclass(Power4, Square)

cube = Cube()
assert cube.get_value(2) == 8
assert cube.get_value(-17) == -4913

power4 = Power4()
assert power4.get_value(5) == 625
assert power4.get_value(25) == 390625

print('Good')
