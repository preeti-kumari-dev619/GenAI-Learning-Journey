class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category
    
    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.__price}")
        print(f"Product Category: {self.category}")
    #get method
    def get_price(self):
        return self.__price
    #set method
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("price updated successfully")
        else:
            print("price must be greater than zero")

        

product1 = Product("Laptop", 6000, "Electronics")
product2 = Product("Headphones", 3000, "Accessories")

product1.get_info()
product2.get_info()

print(f"Current Price: {product1.get_price()}")

print()
product1.set_price(2000)
print("updated product")
product1.get_info()

print()
print("price less then zero")
product1.set_price(-1200)



