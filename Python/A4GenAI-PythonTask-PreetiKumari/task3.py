with open("sales_data.txt", "a") as file:
    file.write("5000\n")
    file.write("2500\n")
    file.write("1700\n")

with open("sales_data.txt", "r") as file:
    print(file.read())

#extra
with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))