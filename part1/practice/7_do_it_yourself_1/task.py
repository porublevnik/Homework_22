#### Блок кода для перехвата вывода в консоль ####
import sys

output_data = []


def print(s):
    if not isinstance(s, str):
        s = str(s)
    sys.stdout.write(s)
    sys.stdout.write('\n')
    output_data.append(s)


#### /Блок кода для перехвата вывода в консоль ####

# Стартвый код

class UnitDied(Exception):
    pass


unit = {
        'name': 'Василий',
        'hp': 10,
        'defense': 1,
        'power': 2,
        'x': 1,
        'y': 1}


def move_unit_up(unit: dict):
    unit['y'] += 1


def move_unit_down(unit: dict):
    unit['y'] -= 1


def move_unit_right(unit: dict):
    unit['x'] += 1


def move_unit_left(unit: dict):
    unit['x'] -= 1


def hit_other_unit(unit: dict, other: dict):
    hit_power = unit['power']
    other_defense = other['defense']
    other['hp'] -= hit_power - other_defense


def get_damage_from_other_unit(unit: dict, other: dict):
    hit_other_unit(unit=other, other=unit)


def check_is_alive(unit: dict):
    if unit['hp'] <= 0:
        raise UnitDied


class Unit:
  def __init__(self, name: str, hp:int, defense: int, power: int, x_coord: int, y_coord: int):
      pass

  def move_up(self):
      pass

  def move_down(self):
      pass

  def move_right(self):
      pass

  def move_left(self):
      pass

  def hit(self, other):
      pass

  def get_damage(self, damage: int):
      pass

  def is_alive(self) -> bool:
      pass


# Данная схватка определенно должна заканчиваться победой Былинного богатыря.
# Код ниже изменять не нужно, его достаточно для того чтобы провести схватку.
unit1 =Unit(name='Басурманин заморский', hp=10, defense=2, power=6, x_coord=1, y_coord=1)
unit2 = Unit(name = 'Богатырь былинный', hp=30, defense=4, power=3, x_coord=1, y_coord=1)
try:
  while all((unit1.is_alive(), unit2.is_alive())):
    unit1.hit(unit2)
    unit2.hit(unit1)
except UnitDied as e:
  print(e.args[0])



# Тесты и код проверки
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_assert(
    output_data == ['Трагически погиб в неравном бою Басурманин заморский',
                   ], correct='Вывод в консоль верный',
    incorrect='Вывод в консоль НЕ верный')

test_assert('Unit' in globals(), correct='Класс Unit успешно создан', incorrect = 'Методы должны быть помещены в класс по имени Unit')
unit = Unit(name='Опытный тыловик', hp=10, defense=1, power=1, x_coord=1, y_coord=1)
test_assert(hasattr(unit, 'name'), correct='У класса Unit есть атрибут "name"', incorrect='У класса Unit отсутствует атрибут "name"')
test_assert(hasattr(unit, 'hp'), correct='У класса Unit есть атрибут "hp"', incorrect='У класса Unit отсутствует атрибут "hp"')
test_assert(hasattr(unit, 'defense'), correct='У класса Unit есть атрибут "defense"', incorrect='У класса Unit отсутствует атрибут "defense"')
test_assert(hasattr(unit, 'power'), correct='У класса Unit есть атрибут "power"', incorrect='У класса Unit отсутствует атрибут "power"')
test_assert(hasattr(unit, 'x'), correct='У класса Unit есть атрибут "x"', incorrect='У класса Unit отсутствует атрибут "x"')
test_assert(hasattr(unit, 'y'), correct='У класса Unit есть атрибут "y"', incorrect='У класса Unit отсутствует атрибут "y"')
unit.move_up()
unit.move_up()
test_assert(unit.y==3, 'Функция "move_up" реализована корректно', incorrect = 'Функция "move_up" реализована НЕ корректно')
unit.move_down()
test_assert(unit.y==2, 'Функция "move_down" реализована корректно', incorrect = 'Функция "move_down" реализована НЕ корректно')
unit.move_left()
test_assert(unit.x == 0, 'Функция "move_left" реализована корректно', incorrect = 'Функция "move_left" реализована НЕ корректно')
unit.move_right()
unit.move_right()
test_assert(unit.x == 2, 'Функция "move_right" реализована корректно', incorrect = 'Функция "move_right" реализована НЕ корректно')
test_unit = Unit(name='Опытный тыловик 2', hp=10, defense=1, power=1, x_coord=1, y_coord=1)
try:
  test_unit.get_damage(damage=11)
  print('Функция get_damage НЕ корректно отрабатывает 0 хп у юнита')
except UnitDied:
  print('Функция get_damage корректно отрабатывает 0 хп у юнита')

test_unit = Unit(name='Опытный тыловик 2', hp=10, defense=4, power=1, x_coord=1, y_coord=1)
test_unit.get_damage(damage=4)
test_assert(test_unit.hp == 10, correct='Защита юнита работает корректно', incorrect="Защита юнита работает НЕ корректно")
