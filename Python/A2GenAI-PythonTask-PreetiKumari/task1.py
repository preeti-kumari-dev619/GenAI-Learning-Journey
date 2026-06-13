order_amount = input("Enter order_amount")
print(order_amount)
if not order_amount.replace('.', '', 1).isdigit():
    print("Error: invalid input please enter a valid numeric value")
    exit()
order_amount = float(order_amount)
if order_amount >= 2000:
    discount_percent = 15
elif order_amount >=1500:
    discount_percent = 10
elif order_amount >= 1000:
    discount_percent = 7
else:
    discount_percent = 0

discount_amount = order_amount * (discount_percent / 100)
final_amount = order_amount - discount_amount

print(f"Order Amount: {order_amount}")
print(f"Discount Amount: {discount_amount}")
print(f"Final Amount: {final_amount}")

#tax
tax = final_amount * 0.05
final_total = final_amount + tax

print(f"Subtotal: {final_amount}")
print(f"Tax: {tax}")
print(f"Final Total: {final_total}")
   