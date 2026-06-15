cart = []
while True:
    try:
        print("Enter price(q to quit):")

        if price.lower() == "q":
            break

        price = float(price)

        if price < 0:
            raise ValueError("price cannot be negative")
        
        cart.append(price)

    except ValueError as error:
        print(f"Error: {error}")

print(f"Total items: {len(cart)}")
print(f"Total bill: {sum(cart)}")