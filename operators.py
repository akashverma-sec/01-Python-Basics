# Arithmetic Operators
a = 20
b = 5

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Power =", a ** b)
print("Floor Division =", a // b)

# Comparison Operators

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Assignment Operators

x = 10

x += 5
print("x += 5 =", x)

x -= 3
print("x -= 3 =", x)

x *= 2
print("x *= 2 =", x)

x /= 4
print("x /= 4 =", x)

# Logical Operators

a = True
b = False

print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)
print("not b =", not b)

# Membership Operators

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)
print("Banana" not in fruits)
print("Orange" not in fruits)

# Identity Operators

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)
print(x is not z)