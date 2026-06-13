#task 4
products = ["jackets", "top", "shirts", "t-shirts", "pants", "trousers"]
price_dict = {
   "jackets": 100,
   "top": 200,
   "shirts": 400,
   "t-shirts": 600,
   "pants": 300,
   "trousers": 500
}

catalog = []
for i in range(len(products)):
    name = products[i]
    price = price_dict[name]
    category = categories[i]
    catalog.append((name, price, category))
print(catalog)
for item in catalog:
    print("", item)

#new dictionary
category_to_products = {}
for name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(name)

print(category_to_products)

#category have maximum products
max_category = max(category_to_products, key=lambda k:len(category_to_products[k]))
print(max_category)
print(category_to_products[max_category])
