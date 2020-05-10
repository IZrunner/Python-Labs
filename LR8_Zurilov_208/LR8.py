class ShopGoods:
    def __init__(self, name="Iron Throne", amount=1, price=123):
        self.__name = name
        self.__amount = amount
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__amount

    @property
    def price(self):
        return self.__price
