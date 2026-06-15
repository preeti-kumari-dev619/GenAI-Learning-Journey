prices = [120, 350, 'abc', 500, -200, 800]
total = 0
for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError
        if price < 0:
            raise ValueError("negative price not allowed")
        total += price
        print(f"running total: {total}")
    
    except TypeError:
        print(f"{price} -> invalid item (not a number)")
    
    except ValueError as error:
        print(f"{price} -> error")


print(f"final total: {total}")