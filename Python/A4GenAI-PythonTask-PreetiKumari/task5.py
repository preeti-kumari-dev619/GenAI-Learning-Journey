# Task 5: Create Product Info File

# Create file and take user input
with open("products.txt", "w") as file:
    
    for i in range(3):
        product_name = input(f"Enter Product {i+1} Name: ")
        price = input(f"Enter Price of {product_name}: ")

        file.write(product_name + " | " + price + "\n")



# Read and display file contents
with open("products.txt", "r") as file:
    
    for line in file:
        product, price = line.strip().split(" | ")

        print("Product Name:", product)
        print("Price: ₹", price)
        print("--------------------")