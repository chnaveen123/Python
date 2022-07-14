class Product:

    def __init__(self, price):
        self.__price = price

    def get_price(self, price):
            return self.__price

    def set_price(self,val):
        if val < 0:
            raise ValueError("Price cannot be less than zero")
        else:
            self.__price = val
