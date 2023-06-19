class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender == "male" or gender == "female":
            self.gender = gender
        else:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = "male"

    def __str__(self):
        if self.gender == "male":
            return f"Гражданин {self.surname} {self.name}"
        else:
            return f"Гражданка {self.surname} {self.name}"



