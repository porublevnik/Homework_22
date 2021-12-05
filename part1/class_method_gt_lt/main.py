# Продолжите прошлое задание, но добавьте методы more, less.
# - Метод more у объекта увеличивает количество товара.
# - Метод less у объекта уменьшает коичество товара. 
#   Если там ничего нет, метод возврашаем False.
#
#   Когда будете тестировать код, обратите внимание 
#   что при вызове метода more у самого класса Storage
#   Мы передаём его качестве аргумента self сам класс
#   тогда как применяя метод экземпляра этого делать не нужно.
#   Это связано с тем, что класс more не обёрнут декоратором @classmethod

class Storage:
    goods_quantity = 10

    def __init__(self, qnt: int):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.goods_quantity = qnt
        else:
            self.goods_quantity = self._get_total()
            self._set_total(0)

    @classmethod
    def _get_total(cls) -> int:
        return cls.goods_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.goods_quantity = qnt
    
    def more(self, qnt: int):
        # TODO напишите логику функции здесь
        pass
    
    def less(self, qnt: int):
        # TODO напишите логику функции здесь
        pass


if __name__ == '__main__':
    print("Всего на складе: ", Storage.goods_quantity)
    Storage.more(Storage, qnt=4)
    print("Число товаров на складе увеличено до:", Storage.goods_quantity)
    Storage.less(Storage, qnt=3)
    print("Число товаров на складе уменьшено до:", Storage.goods_quantity)
    Storage.more(Storage, qnt=10)
    print("Число товаров на складе увеличено до:", Storage.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 6 ед. со склада)")
    storage = Storage(6)
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Используем метод more экземпляра класса Goods (попытаемся добавить 2 ед. товара 'со стороны')")
    storage.more(qnt=2)
    print("К отгруженным товарам прибавилось 2 ед.:", storage.goods_quantity)
    print("На складе число товаров осталось без изменения:", Storage.goods_quantity)