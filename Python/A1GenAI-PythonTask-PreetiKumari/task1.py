#task 1
#list
products = ["jackets", "top", "shirts", "t-shirts", "pants", "trousers"]

#tuple
sample_products = ("jackets", 500, "cloth")

#second product of list
print(products[1])

#last product of list
print(products[-1])

#add new products to list
products.append("jeans")
products.append("sweater")

#updated product list
print(products)

#change tuple to list
sample_list = list(sample_products)
print(type(sample_list))

#price change
sample_list[1] = 400
print(sample_list)

#again in tuple
sample_tuple = tuple(sample_list)
print(type(sample_tuple))