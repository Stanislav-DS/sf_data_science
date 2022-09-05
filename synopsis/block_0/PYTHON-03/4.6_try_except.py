try:
    a = int(input("Enter a number >>\t"))
except ValueError:
    print("Wrong input")
else:
    print("You entered a right number")
finally:
    print("Exit")
