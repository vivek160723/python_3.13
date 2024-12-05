class Product:
    discount = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price * (1 - Product.discount)

    @classmethod
    def set_discount(cls, discount_percentage):
        if 0 <= discount_percentage <= 1:
            cls.discount = discount_percentage
        else:
            raise ValueError("Discount must be between 0 and 1")


# Create a list of products
products = [
    Product("Laptop", 1000),
    Product("Phone", 800),
    Product("Tablet", 500),
    Product("Headphones", 200)
]

# Set a discount for all products
Product.set_discount(0.2)

# Print prices with the discount applied
print("\nPrices with 20% discount:")
for product in products:
    print(f"{product.name}: ${product.get_price():.2f}")



#########################################################################################
# class Product:
#     discount = 0.0
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def get_price(self):
#         return self.price * (1 - Product.discount)
#
#     @classmethod
#     def set_discount(cls, discount_percentage):
#         if 0 <= discount_percentage <= 1:
#             cls.discount = discount_percentage
#         else:
#             raise ValueError("Discount must be between 0 and 1")
#
#
# product1 = Product("Laptop", 1000)
# product2 = Product("Phone", 800)
#
# Product.set_discount(0.2)
#
# print("\nPrices with 20% discount:")
# print(f"{product1.name}: ${product1.get_price():.2f}")
# print(f"{product2.name}: ${product2.get_price():.2f}")













