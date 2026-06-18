class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"
    
    def __add__(self, other):
        return self.price + other.price
    

product1 = Product("Laptop", 60000)
product2 = Product("Headphones", 50000)


print(f"Product 1: {product1}")
print(f"Product 2: {product2}")

total_price = product1 + product2
print(f"Total Price: {total_price}")