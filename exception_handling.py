try:
    number = int(input("Enter a number: "))
    print("Your number is:", number)

except ValueError:
    print("Invalid input! Please enter a number.")