def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("age must be between 1 and 120")
    print(f"valid age: {age}")


try:
    age = int(input("Enter your age:"))
    check_age(age)

except ValueError as error:
    print(error)