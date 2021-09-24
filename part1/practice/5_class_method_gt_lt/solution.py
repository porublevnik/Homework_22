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


#Решение
class Goods:
    total_quantity = 0

    def __init__(self, qnt: int):
        if qnt < self._get_total():
            self.quantity = qnt
            self._set_total(self._get_total() - qnt)

        else:
            print(f'Некомплект. Осталось всего {self._get_total()} а нужно {qnt}')
            self.quantity = self._get_total()
            self._set_total(0)
        print(f'Создан объект {self.__class__.__name__}. Количество {self.quantity}. Осталось {self._get_total()}')

    def more(self, qnt: int):
        if self._get_total() == 0:
            return False
        if self._get_total() < qnt:
            qnt = self._get_total()
        self._set_total(self._get_total() - qnt)
        self.quantity += qnt
        self._report()


    def less(self, qnt: int):
        if self.quantity < qnt:
            qnt = self.quantity
        self._set_total(self._get_total() + qnt)
        self.quantity -= qnt
        self._report()

    def _report(self):
        print(f'Теперь у объекта {self.__class__.__name__} {self.quantity} единиц. На складе {self._get_total()}')

    @classmethod
    def _get_total(cls) -> int:
        return cls.total_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.total_quantity = qnt


class Python(Goods):
    total_quantity = 10

    def __init__(self, qnt: int):
        super(Python, self).__init__(qnt=qnt)


class Book(Goods):
    total_quantity = 10

    def __init__(self, qnt: int):
        super(Book, self).__init__(qnt=qnt)


class Coffe(Goods):
    total_quantity = 10

    def __init__(self, qnt: int):
        super(Coffe, self).__init__(qnt=qnt)

python = Python(qnt=4)
python.more(qnt=4)
python.less(qnt=3)
python.more(qnt=10)
print(python.more(qnt=1))


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])

test_assert(
    output_data == ['Создан объект Python. Количество 4. Осталось 6',
                    'Теперь у объекта Python 8 единиц. На складе 2',
                    'Теперь у объекта Python 5 единиц. На складе 5',
                    'Теперь у объекта Python 10 единиц. На складе 0',
                    'False'], correct='Вывод в консоль верный', incorrect='Вывод в консоль НЕ верный')