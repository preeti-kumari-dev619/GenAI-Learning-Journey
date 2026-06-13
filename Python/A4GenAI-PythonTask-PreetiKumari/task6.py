import os
filename = input("Enter the filename to open:")
if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("file not found. please check the filename.")