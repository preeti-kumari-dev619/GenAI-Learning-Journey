daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0
for day_value in daily:
    if day_value == -1:
        print("corrupted data found, stopping")
        break
    if day_value == 0:
        print("No sales today.skipping")
        continue
    total_sales += day_value
    print(f"valid sales: {day_value} | Running total: total_sales")
print(total_sales)