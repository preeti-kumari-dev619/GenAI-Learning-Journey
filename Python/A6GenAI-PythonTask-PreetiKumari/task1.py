try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator

except ValueError:
    print("Invalid input! please enter numbers only")

except ZeroDivisionError:
    print("Denominator cannot be 0.") 

else:
    print(f"Result: {result}")

finally:
    print("operation complete")