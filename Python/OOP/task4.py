class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")

class Laptop(Product):
    def get_info(self):
        print(f"Laptop Name: {self.name}")
        print(f"Proce: {self.price}")


class Mobile(Product):
    def get_info(self):
        print(f"Mobile Name: {self.name}")
        print(f"Price: {self.price}")


laptop1 = Laptop("Hp Pavillian", 65000)
mobile1 = Mobile("Sumsung Galaxy", 30000)


products = [laptop1, mobile1]

for product in products:
    product.get_info()