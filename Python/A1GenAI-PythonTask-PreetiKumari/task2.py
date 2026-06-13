#task 2
categories = ["Outwear", "Tops", "Tops", "Tops", "Bottoms", "Bottoms"]
categories_set = set(categories)
print(categories_set)

#new category
categories_set.add("footwear")
print(categories_set)

#duplicates ignored
categories_set.add("Tops")
print(categories_set)

#categories exist in set
print("Tops" in categories_set)
print("Suits" in categories_set)

#total categories
print(len(categories_set))