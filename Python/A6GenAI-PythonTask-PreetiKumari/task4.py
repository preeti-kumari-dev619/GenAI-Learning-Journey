filename = input("Enter Filename:")
try:
    file = open(filename, "r")
    
    for i in range(3):
        print(file.readline())

except FileNotFoundError:
    print("file not found")

except PermissionError:
    print("permission denied")

else:
    file.close()

finally:
    print("file attempt completed")
    
