class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
        print(f"Product Category: {self.category}")
        
    
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years
    

    def get_info(self):
        print(f"Product name: {self.name}")
        print(f"Product Price: {self.price}")
        print(f"Product Category: {self.category}")
        print(f"Product Warranty Years: {self.warranty_years}")


product1 = ElectronicProduct("Laptop", 6000, "Electronics", 2)

product1.get_info()