class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"category: {self.category}")


    def __add__(self, other):
        return self.price + other.price
    

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} removed successfully")
                return
            
        print("Product not found")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def show_all_products(self):
        for product in self.products:
            product.get_info()
            print()


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, name, price, category):
        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"Store Name: {self.store_name}")
        print(f"Total items: {len(self.inventory.products)}")
        print(f"Total Values: {self.inventory.get_total_value()}")
        self.inventory.show_all_products()


store = Store("Tech Electronics")


store.add_new_product("Laptop", 6000, "Electronics")
store.add_new_product("Headphones", 3000, "Accessories")
store.add_new_product("Mobile", 2500, "Electronics")


store.show_summary()

product1 = store.inventory.products[0]
product2 = store.inventory.products[1]
total_price = product1 + product2
print(f"Comnined Price: {total_price}")