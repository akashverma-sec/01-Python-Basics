# Notes Manager

note = input("Write your note: ")

with open("my_notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved successfully!")

print("\nAll Notes:")

with open("my_notes.txt", "r") as file:
    print(file.read())