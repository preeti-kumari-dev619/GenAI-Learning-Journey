orders = []
while True:
    print("Order Menu")
    print("1-Add order amount")
    print("2-show all orders and totals")
    print("q-Quit")

    choice = input("Enter Your Choice:")
    if choice == "q":
        print("Exiting Program")
        break
    elif choice == "1":
        amount_input = input("Enter Order Amount:")
        if not amount_input.replace('.', '', 1).isdigit():
           print("invalid amount, Try again")
           continue
        orders.append(float(amount_input))
        print("Orders added")
    elif choice == "2":
        if len(orders) == 0:
            print("No orders yet")
            continue
        print("Orders Amount | Discount% | Final Amount")
        print("-" * 42)
        total_revenue = 0

        for order_amount in orders:
            if order_amount >= 2000:
                discount_percent = 15
            elif order_amount >= 1500:
                discount_percent = 10
            elif order_amount >= 1000:
                discount_percent = 7
            else:
                discount_percent = 0
            
            final_amount = order_amount - order_amount * (discount_percent / 100)
            total_revenue += final_amount
            print(str(order_amount) + "    | " + str(discount_percent) + "%   | " + str(final_amount))
        print("-" * 42)
        print("Total Revenue:", total_revenue)
    else:
        print("Invalid choice. Please enter 1, 2, or q.")
        continue