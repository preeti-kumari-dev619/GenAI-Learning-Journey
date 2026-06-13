orders = [1200, 2500, 800, 1750, 3000]
print("Order Amount | Discount% | Final Amount")
print("-" * 42)
total_revenue = 0
discounted_count = 0

for orders_amount in orders:
    if orders_amount >= 2000:
        discount_percent = 15
    elif orders_amount >= 1500:
        discount_percent = 10
    elif orders_amount >= 1000:
        discount_percent = 7
    else:
        discount_percent = 0
    discount_amount = orders_amount * (discount_percent / 100)
    final_amount = orders_amount -  discount_amount
    total_revenue += final_amount

# discount_percent>0
    if discount_percent > 0:
        discounted_count += 1
    print(str(orders_amount) + "         | " + str(discount_percent) + "%        | " + str(final_amount))


print("-" * 42)
print("Total Revenue after discounts:", total_revenue)

# OPTIONAL EXTRA
print("Orders that received a discount:", discounted_count)