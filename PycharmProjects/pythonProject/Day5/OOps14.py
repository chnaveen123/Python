class  Product:

    def __init__(self,price):
        self.__price = price

    @property
    def price(self):
        print("getter called")
        return f"The price if {self.__price}"

    @price.setter
    def 