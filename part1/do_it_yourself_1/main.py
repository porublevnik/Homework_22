# Стартовый код

# Вам предоставлены функции, соберите их в класс Unit.
# C помощью этих функций реализовано 
# поведение игрового юнита (в тестовом примере он представлены словарем). 
# Пожалуй, не стоит хранить такую важную сущность в простом словаре - лучше 
# сделаем из него собственный класс.
# В примере Также приведен шаблон класса с именами функций, 
# которые нужно корректно реализовать опираясь на функции, 
# которые были представлены в начале.

# Обратите внимание на параметр other у метода hit. 
# В него в качестве значения будет передан тот юнит 
# по которому мы будем наносить удар
import random

# функции, необходимые для реалзиации юнита:
# их вам будет достаточно, чтобы написать собственный класс
unit_1 = {
    "name": "Случайны богатырь",
    "hp": 20,
    "power": 3,
    "defence": 2,
}

def hit(unit, other):
    damage = random.choice(range(1, unit.get("power")))
    name = unit.get("name")
    hp = unit.get("hp")
    other_name = other.get("name")
    other_hp = other.get("hp")
    get_damage(other, damage)
    return f"{name} ({hp}) наносит {damage} урона {other_name} ({other_hp})"


def get_damage(unit, damage):
    if unit.get("defence") < damage:
        unit["hp"] -= damage - unit.get("defence")
    is_alive(unit)

def is_alive(unit):
    name = unit.get("name")
    if unit.get("hp") <= 0:
        raise UnitDied(f'Трагически погиб в неравном бою {name}')
    return True

# Исключение для реализации гибели юнита, его не нужно менять
class UnitDied(Exception):
    pass

# TODO реализуйте класс Unit ниже

import random

class UnitDied(Exception):
    pass


class Unit:
    def __init__(self, name, hp, defence, power):
        self.name = name
        self.hp = hp
        self.defence = defence
        self.power = power

    def hit(self, other):
        damage = random.choice(range(1, self.power))
        other.get_damage(damage)
        return f"{self.name} ({self.hp}) наносит {damage} урона {other.name} ({other.hp})"

    def get_damage(self, damage):
        if damage > self.defence:
            self.hp -= (damage - self.defence)
        self.is_alive()

    def is_alive(self):
        if self.hp <= 0:
            raise UnitDied(f'Трагически погиб в неравном бою {self.name}')
        return True


# Данная схватка должна заканчиваться победой Былинного богатыря.
# Но иногда случаются неудачи.. :) код ниже изменять не нужно, 
# его достаточно для того чтобы провести схватку,
# когда у Вас будет готовый класс. Если вдруг схватка затянется, прервите её с помощью
# сочетания клавиш ctrl - C
if __name__ == "__main__":
    unit1 = Unit(name='Басурманин заморский', hp=10, defence=1, power=5)
    unit2 = Unit(name='Богатырь былинный', hp=30, defence=2, power=3)
    try:
        while all((unit1.is_alive(), unit2.is_alive())):
            print(unit1.hit(unit2))
            print(unit2.hit(unit1))
    except UnitDied as e:
        print(e.args[0])
