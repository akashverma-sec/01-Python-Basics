print("=== Safe Calculator ===")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Result =", num1 + num2)

    elif operator == "-":
        print("Result =", num1 - num2)

    elif operator == "*":
        print("Result =", num1 * num2)

    elif operator == "/":
        print("Result =", num1 / num2)

    else:
        print("Invalid Operator!")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Thank you for using Safe Calculator!")