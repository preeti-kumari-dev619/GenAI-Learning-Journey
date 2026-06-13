#Task 3
price_dict = {
   "jackets": 100,
   "top": 200,
   "shirts": 400,
   "t-shirts": 600,
   "pants": 300,
   "trousers": 500
}

price_dict["shoes"] = 700
print(price_dict)

#update
price_dict.update({"shirts": 800})
print(price_dict)

#remove
product_remove = "eyes"
if product_remove in price_dict:
    del price_dict[product_remove]
    print(f"{product_remove} removed")
else:
    print(f"{product_remove} does not exist")


#average price
total = sum(price_dict.values())
count = len(price_dict)
average = total / count
print(average)

#min max
max_product = max(price_dict, key=lambda k: price_dict[k])
min_product = min(price_dict, key=lambda k: price_dict[k])
print(f"max-price:{price_dict[max_product]}")
print(f"min-price:{price_dict[min_product]}")