# Task 2
with open("sales_data.txt", "r") as file:
    print("using read():")
    print(file.read())

with open("sales_data.txt", "r") as file:
    first_line = file.readline()
    print(first_line)

with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    sales = []
    for line in lines:
        sales.append(int(line.strip()))
    print(sales)