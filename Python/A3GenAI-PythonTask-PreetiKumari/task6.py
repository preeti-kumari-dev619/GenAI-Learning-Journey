def process_prices(prices):
    discounted_prices = list(map(lambda p: p - (p * 10 / 100), prices))
    filtered_prices   = list(filter(lambda p: p > 300, discounted_prices))
    return discounted_prices, filtered_prices

# Test
discounted, filtered = process_prices([100, 500, 900, 50, 750])

print("Discounted prices :", discounted)
print("Filtered (>300)   :", filtered)