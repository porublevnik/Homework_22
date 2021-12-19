# Вам предоставлен класс не соответствующий принципу "инкапсуляции", 
# перепишите его так, чтобы он стал соответствовать
#
# Логика работы класса такова:
# Класс представляет собой магазин.
# У магазина есть 2 внешние функции:
# - добавление товара на склад извне (add_item)
# - выдача товара (get_item)
# И 2 внутренние функции:
# - проверяем остался ли товар на складе (check_item)
# - узнаем, сколько товара на складе у нас осталось (_check_quantity_limits)
#
# Если какого-то из предметов, которые мы будем хранить 
# на складе будет меньше чем запрошено,
# то нужно возвращать все, осталось на складе.
#
# Если какого-то из предметов на складе и не было - Нужно сообщать 
# 'Не было на складе'
#
# Ваша задача:
# 1. Создайте в классе Store аттрибут store, в котором будет храниться 
#    информация о товарах.
# 2. Проверьте остальные функции и переименуйте соответствующим образом переменную store
# 3. Перенесите функцию check_item в тело класса и сделайте её приватным методом
# 4. Попробуйте запустить файл, должно всё сработать корректно=)


def check_item(store, title):
    return title in store


class Store:
    def add_item(self, store, title, quantity):
        store[title] = store.get(title, 0) + quantity

    def get_item(self, store, title, quantity):
        if not check_item(store=store, title=title):
            return 'Не было на складе'
        quantity = self._check_quantity_limits(store=store, title=title, quantity=quantity)
        store[title] -= quantity
        return title, quantity

    def _check_quantity_limits(self, store, title, quantity):
        current_qnt = store[title]
        if current_qnt < quantity:
            quantity = current_qnt
        return quantity


if __name__ == '__main__':
    # Код ниже является проверочным и должен выполняться корректно
    my_store = Store()
    my_store.add_item(title='Сушеные питоны', quantity=10)
    my_store.add_item(title='Сушеные питоны', quantity=10)
    my_store.add_item(title='Сырые питоны', quantity=5)
    print(my_store.get_item(title='Сушеные питоны', quantity=20))
    print(my_store.get_item(title='Сырые питоны', quantity=10))
    print(my_store.get_item(title='Сырые питоны', quantity=10))
    print(my_store.get_item(title='Админские барабаны', quantity=7))

