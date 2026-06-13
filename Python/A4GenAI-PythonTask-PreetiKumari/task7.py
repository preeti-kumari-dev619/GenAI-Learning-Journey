prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}
discount = float(input("Enter the Discount Percentage:"))
with open("discount_report.txt", "w") as file:
    file.write("Product | Original Price | Discounted Price\n")
    file.write("----------------------------------------------- \n")
    total_discounted_price = 0
    for product,price in prices.items():
        discounted_price = price - price * (discount / 100)
        file.write(f"{product} | {str(price)} | {str(discounted_price)} \n")
        total_discounted_price += discounted_price


    #extra
    total_items = len(prices)
    avg_discounted_prices = total_discounted_price / total_items

    file.write("\n")
    file.write(f"Total items: {str(total_items)}  \n")
    file.write(f"Average Discounted Price: {str(avg_discounted_prices)} \n")

with open("discount_report.txt", "r") as file:
    print(file.read())