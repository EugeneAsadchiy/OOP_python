# Напишите определение классов Person Company Employee
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Person: {self.name}, {self.age}")


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f"Company: {self.company_name}, {self.location}")


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super().__init__(name, age)
        Company.__init__(self, company_name, location)

# Ниже расположены провевки для кода


a = Person('Ivan', 32)
a.display_person_info()

a = Company('Zara', 'Prague')
a.display_company_info()

emp = Employee('Jessica', 28, 'Google', 'Atlanta')
emp.display_person_info()
emp.display_company_info()

emp2 = Employee('Kolya', 11, 'Facebook', 'Seatle')
emp2.display_person_info()
emp2.display_company_info()