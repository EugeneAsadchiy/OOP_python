# Напишите определение класса Hero
class Hero:
    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        if self.__len__() == 0:
            return ""
        else:
            answer = ""
            for key, value in sorted(self.__dict__.items()):
                answer += f"{key}: {value}\n"
        return answer.rstrip('\n')


# Ниже код для проверки методов класса Hero
hero = Hero()
assert len(hero) == 0
hero.health = 50
hero.damage = 10
assert len(hero) == 2
assert str(hero) == '''damage: 10
health: 50'''
hero.weapon = ['sword', ' bow']
hero.skill = 'Некромант'
assert str(hero) == '''damage: 10
health: 50
skill: Некромант
weapon: ['sword', ' bow']'''
print(hero)

villain = Hero()
assert str(villain) == ''
assert len(villain) == 0
villain.level = 15
villain.skill = 'Боец'
villain.armor = 25
assert len(villain) == 3
assert str(villain) == '''armor: 25
level: 15
skill: Боец'''
print(villain)
