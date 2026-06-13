sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as f:
    for sale in sales:
        f.write(str(sale) + "\n")

print("=== File Contents (one per line) ===")
with open("sales_data.txt", "r") as f:
    print(f.read())

#extra
with open("sales_data_csv.txt", "w") as f:
    f.write(",".join(str(s) for s in sales) + "\n")

print("=== File Contents (comma-separated) ===")
with open("sales_data_csv.txt", "r") as f:
    print(f.read())

