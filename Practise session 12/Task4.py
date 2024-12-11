class Product:
    def __init__(self, price, stock):
        self.__price = 0
        self.__stock = 0
        self.price = price
        self.stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price cannot be negative")

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value >= 0:
            self.__stock = value
        else:
            raise ValueError("Stock cannot be negative")

product = Product(100, 50)
print(f"Price: {product.price}, Stock: {product.stock}")
product.price = 120
product.stock = 30
print(f"Updated Price: {product.price}, Updated Stock: {product.stock}")

