# Продолжите прошлое задание, но добавьте методы more, less.
# - Метод more у объекта увеличивает количество товара в экземпляре класса
#   на заданное число и одновременно с этим уменьшает 
#   число товаров на складе на это же число.
# - Метод less у объекта уменьшает количество товара в экземпляре класса на
#   заданное число, одновременно с этим увеличивает число 
#   товара на складе на это же число


class Storage:
    goods_quantity = 15

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
        if self._get_total() > qnt:
            self.goods_quantity += qnt
            self._set_total(self._get_total() - qnt)
        else:
            self.goods_quantity += self._get_total()
            self._set_total(0)

    def less(self, qnt):
        if self.goods_quantity > qnt:
            self.goods_quantity -= qnt
            self._set_total(self._get_total() + qnt)
        else:
            self._set_total(self._get_total() + self.goods_quantity)
            self.goods_quantity = 0



if __name__ == '__main__':
    print("Всего на складе: ", Storage.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 6 ед. со склада)")
    storage = Storage(6)
    print("Отгружаем 5 ед. товара со склада в экземпляр класса")
    storage.more(5)
    print("Число отгруженных товаров возросло до:", storage.goods_quantity)
    print("Остаток на складе: ", Storage.goods_quantity)
    storage.less(4)
    print("Число отгруженных товаров сократилось до:", storage.goods_quantity)
    print("Остаток на складе: ", Storage.goods_quantity)
    storage.less(8)
    print("Число отгруженных товаров сократилось до:", storage.goods_quantity)
    print("Остаток на складе: ", Storage.goods_quantity)