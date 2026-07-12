# Tuple Example

colors = ("red", "green", "blue", "yellow", "orange")
print(colors)
print(type(colors))
print(colors[0])
print(colors[-1])

#Dictionary Example

student = {
    "name": "Akash",
    "age": 20,
    "course": "MCA"
}
print(student)
print(student["name"])
print(student["course"])

# Set Example

numbers = {10, 20, 30, 20, 40, 10}
print(numbers)
numbers.add(50)
print("After add:", numbers)
numbers.remove(20)
print("After remove:", numbers)
