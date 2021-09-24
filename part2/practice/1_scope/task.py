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

# Стартовый код

# Класс Goods менять нельзя
class Goods:
    units = 'л.'
    quantity = 3

    def __init__(self, title: str, **kwargs):
        self.title = title

    def prnt(self):
        print(f'{self.title} {self.quantity} {self.units}')


class Coffee(Goods):
    def __init__(self, **kwargs):
        super(Coffee, self).__init__(**kwargs)


class Water(Goods):
    def __init__(self, **kwargs):
        super(Water, self).__init__(**kwargs)


class Cookies(Goods):
    def __init__(self, **kwargs):
        super(Cookies, self).__init__(**kwargs)


my_coffee = Coffee(title='Кофе', units='г.', quantity=3)
another_coffee = Coffee(title='Кофе', units='ведр.')
my_water = Water(title='Вода', units='л.', quantity=4)
another_water = Water(title='Вода', quantity=5)
my_cookies = Cookies(title='Печеньки', units='уп.', quantity=1)

my_coffee.prnt()
my_water.prnt()
my_cookies.prnt()
another_water.prnt()
another_coffee.prnt()


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_coffee = Coffee(title='Кофе', units='г.', quantity=5)
test2_coffee = Coffee(title='Много кофе')

test_assert(
    output_data == ['Кофе 3 г.',
                    'Вода 4 л.',
                    'Печеньки 1 уп.',
                    'Вода 5 л.',
                    'Кофе 3 ведр.'], correct='Вывод в консоль верный',
    incorrect='Вывод в консоль НЕ верный')

test_assert(all((test_coffee.units == 'г.', test2_coffee.units == 'л.')), correct='Затенение units реализовано верно',
            incorrect='Затенение units реализовано НЕ верно')

test_assert(all((test_coffee.quantity == 5, test2_coffee.quantity == 3)),
            correct='Затенение quantity реализовано верно', incorrect='Затенение quantity реализовано НЕ верно')
