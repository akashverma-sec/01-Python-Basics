# Try and Except Example

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid Input! Please enter only numbers.")


# Zero Division Example

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result =", a / b)

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")    


# Else Example

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input!")
else:
    print("You entered:", num)    


# Finally Example

try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Invalid Input!")

finally:
    print("Program Finished.")    