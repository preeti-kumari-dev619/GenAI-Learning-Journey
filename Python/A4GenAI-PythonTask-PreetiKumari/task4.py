with open("sales_data.txt", "r") as file:
    lines = file.readlines()
sales = []
for line in lines:
    sales.append(int(line.strip()))
total_sales = sum(sales)
hightest_sales = max(sales)
lowest_sales = min(sales)
avg_sales = total_sales / len(sales)

print(f"Total Sales: {total_sales}")
print(f"Highest Sales: {hightest_sales}")
print(f"Lowest Sales: {lowest_sales}")
print(f"Average Sales: {avg_sales}")