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


# Решение
class Store:
    def __init__(self):
        self.store = {}

    def add_item(self, title: str, quantity: int):
        self.store[title] = self.store.get(title, 0) + quantity

    def get_item(self, title, quantity):
        if not self._check_item(title=title):
            return 'Не было на складе'
        quantity = self._check_quantity_limits(title=title, quantity=quantity)
        self.store[title] -= quantity
        return title, quantity

    def _check_item(self, title: str):
        return title in self.store

    def _check_quantity_limits(self, title: str, quantity: int) -> int:
        current_qnt = self.store[title]
        if current_qnt < quantity:
            quantity = current_qnt
        return quantity

my_store = Store()
my_store.add_item(title='Сушеные питоны', quantity=10)
my_store.add_item(title='Сушеные питоны', quantity=10)
my_store.add_item(title='Сырые питоны', quantity=5)
print(my_store.get_item(title='Сушеные питоны', quantity=20))
print(my_store.get_item(title='Сырые питоны', quantity=10))
print(my_store.get_item(title='Сырые питоны', quantity=10))
print(my_store.get_item(title='Админские барабаны', quantity=7))



# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_assert(
    output_data == ["('Сушеные питоны', 20)",
                    "('Сырые питоны', 5)",
                    "('Сырые питоны', 0)",
                    "Не было на складе"
                    ], correct='Вывод в консоль верный',
    incorrect='Вывод в консоль НЕ верный')

test_store = Store()
test_assert(hasattr(test_store, 'store'), correct='Атрибут store присутствует в классе Store', incorrect='Атрибут store отсутствует в классе Store')
test_assert(isinstance(test_store.store, dict), correct='Атрибут store верно реализован словарем', incorrect='Атрибут store должен быть реализован словарем')
