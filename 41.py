# Напишите определение класса DictMixin
class DictMixin:
    def to_dict(self):
        answer = dict()

        for key, value in self.__dict__.items():
            d = dict()
            # print(answer)
            if isinstance(value, DictMixin):
                # print(value.__dict__)
                for i, j in value.__dict__.items():
                    d.update([(i, j)])
                answer.update([(key, d)])
            elif isinstance(value, list):
                spisok=[]
                for names in value:
                    driens = dict()
                    for key1, value1 in names.__dict__.items():
                        if isinstance(value1, DictMixin):
                            d = dict()
                            # print(value.__dict__)
                            for l, m in value1.__dict__.items():
                                d.update([(l, m)])
                            driens.update([(key1, d)])
                        else:
                            driens.update([(key1, value1)])

                    spisok.append(driens)
                answer.update([(key, spisok)])
            else:
                answer.update([(key, value)])
        return answer


# Ниже код для проверки миксина DictMixin

class Phone(DictMixin):
    def __init__(self, number):
        self.number = number


class Person(DictMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(DictMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(DictMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


address = Address("123 Main St", "Anytown", "CA", "12345")
john_doe = Person("John Doe", 30, address)

john_doe_dict = john_doe.to_dict()

assert john_doe_dict == {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip_code': '12345'
    }
}

address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_dict() == {
    'street': '123 Main St',
    'city': 'Albuquerque',
    'state': 'NM',
    'zip_code': '987654'
}
walter = Person("Walter White", 30, address)
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White'}

walter_phone = Phone("555-1234")
walter.phone = walter_phone
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White',
                            'phone': {'number': '555-1234'}}

company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
company = Company("SCHOOL", company_address)

assert company.to_dict() == {'address': {'city': 'Albuquerque',
                                         'state': 'NM',
                                         'street': '3828 Piermont Dr',
                                         'zip_code': '12345'},
                             'name': 'SCHOOL'}

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
jesse.phone = Phone("555-5678")

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_dict() == {'address': {'city': 'Albuquerque',
                                       'state': 'NM',
                                       'street': 'Los Pollos Hermanos',
                                       'zip_code': '12345'},
                           'age': 55,
                           'friends': [{'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '123 Main St',
                                                    'zip_code': '987654'},
                                        'age': 30,
                                        'name': 'Walter White',
                                        'phone': {'number': '555-1234'}},
                                       {'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '456 Oak St',
                                                    'zip_code': '12345'},
                                        'age': 27,
                                        'name': 'Jesse Bruce Pinkman',
                                        'phone': {'number': '555-5678'}}],
                           'name': 'Gustavo Fring'}

print('Good')
