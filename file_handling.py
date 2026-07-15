# Write to a File

file = open("notes.txt", "w")

file.write("Hello Akash!\n")
file.write("Welcome to Python File Handling.")

file.close()

print("Data written successfully.")

# Read File

file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()

# Append Data

file = open("notes.txt", "a")

file.write("\nThis is a new line added using Append Mode.")

file.close()

print("Data appended successfully.")

# Using with open()

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)