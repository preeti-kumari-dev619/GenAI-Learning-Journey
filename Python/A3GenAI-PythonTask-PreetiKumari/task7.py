def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    return max(prices_list)

# Menu
prices_list = []

while True:
    print(" Add price")
    print("2 Show average price")
    print("3 Show highest price")
    print("q Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices_list, price)
        print("Price added. List:", prices_list)

    elif choice == "2":
        if len(prices_list) == 0:
            print("No prices added yet.")
        else:
            print("Average price:", get_average_price(prices_list))

    elif choice == "3":
        if len(prices_list) == 0:
            print("No prices added yet.")
        else:
            print("Highest price:", get_max_price(prices_list))

    elif choice == "q":
        print("Exiting menu.")
        break

    else:
        print("Invalid choice. Try again.")