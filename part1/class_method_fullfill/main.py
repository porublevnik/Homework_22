# Продолжите прошлое задание, реализуйте для 
# каждого из трех классов метод fulfill, который 
# бы полностью отгружал все имеющиеся товары
# со склада (класса) в экземпляр класса.
# В этом методе можно использовать имеющиеся методы класса и экземпляра
# Попробуйте поэксперементировать с кодом в блоке if __name__ == __main__

class Storage:
    goods_quantity = 10

    def __init__(self, qnt):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.goods_quantity = qnt
        else:
            self.goods_quantity = self._get_total()
            self._set_total(0)

    @classmethod
    def _get_total(cls):
        return cls.goods_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.goods_quantity = qnt
    
    def more(self, qnt):
        self.goods_quantity += qnt
    
    def less(self, qnt: int):
        if self.goods_quantity < qnt:
            return False
        else:
            self.goods_quantity -= qnt

    def fullfill(self):
        # TODO напишите логику функции здесь
        pass
        


# Посмотрите, что происходит с классом при применении различных методов.
# Можете поэксперементировать и попробовать добавить свои.
if __name__ == '__main__':
    print("Всего на складе: ", Storage.goods_quantity)
    Storage.more(Storage, qnt=4)
    print("Число товаров на складе увеличено до:", Storage.goods_quantity)
    Storage.less(Storage, qnt=3)
    print("Число товаров на складе уменьшено до:", Storage.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 4 ед. со склада)")
    python = Storage(qnt=4)
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Отгрузили со склада в экземпляр класса:", python.goods_quantity)
    print("Отгружаем все имеющиеся товары со склада в экземпляр класса:")
    python.fullfill()
    print("Осталось на складе:", Storage.goods_quantity)
    print("Имеется в экземпляре:", python.goods_quantity)
