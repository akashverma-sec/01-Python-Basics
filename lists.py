# lists
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[1:3])
print(fruits[2:])
print(fruits[:2])

# List Methods

fruits.append("grapes")
print("after append:", fruits)
fruits.insert(1, "blueberry")
print("after insert:", fruits)
fruits.remove("banana")
print("after remove:", fruits)
fruits.pop()
print("after pop:", fruits)

# Loop with lists

print("\nAll fruits:")
for fruit in fruits:
    print(fruit)