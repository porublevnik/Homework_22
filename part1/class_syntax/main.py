#  Реализуйте класс товара (Item) с аттрибутами:
#    - название(title)
#    - цена(price)   
# 
#  Реализуйте класс чек (Cheque) который должен содержать:
#    Аттрибут items (должен представлять собой список).
#    (В блоке if __name__ == "__main__" мы добавим туда покупки)
#
# Метод purchases, который должен вернуть строку вида:
# Сушеные питоны - 500
# Книги про PHP - 10
# Кофе плохорастворенный - 200
#
# Метод get_sum, который должен вернуть строку вида:
# Всего: 710

# Стартовый код


class Item:
    def __init__(self, title, price):
        pass
        # TODO напишите Ваш код здесь

class Cheque:
    def __init__(self):
        pass
        # TODO напишите Ваш код здесь

    def purchases(self):
        pass
        # TODO напишите Ваш код здес
    
    def get_sum(self):
        pass
        # TODO напишите Ваш код здес

if __name__ == '__main__':
    # Создаём товары с ценой
    dry_pythons = Item(title='Сушеные питоны', price=500)
    php_books = Item(title='Книги про PHP', price=700)
    questionable_coffe = Item(title='Кофе плохорастворенный', price=200)
    # Создаём чек
    cheque = Cheque()
    # Добавляем товары в чек
    cheque.items.extend([dry_pythons, php_books, questionable_coffe])
    # Печатаем чек
    print(cheque.purchases())
    print(cheque.get_sum())