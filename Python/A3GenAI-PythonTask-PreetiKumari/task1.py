def apply_discount(price, discount_percent=5):
    if discount_percent > 60:
       discount_percent = 60
    discounted_price = price - (price * discount_percent / 100)
    return discounted_price

print(apply_discount(1000, 10))
print(apply_discount(500))
print(apply_discount(1000, 70))
