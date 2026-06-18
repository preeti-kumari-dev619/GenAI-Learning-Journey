class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
        print(f"Product Category: {self.category}")
    
    def apply_discount(self, percent):
        discount_amount = (self.price * percent) / 100
        discounted_price = self.price - discount_amount
        return discounted_price

product1 = Product("Laptop", 6000, "Electronics")
product2 = Product("Headphones", 3000, "Accessories")

product1.get_info()
product2.get_info()
print()
print("Discount Price")
print()
print(f"Discounted Laptop Price: {product1.apply_discount(10)}")
print(f"Discounted Headphone Price: {product2.apply_discount(20)}")