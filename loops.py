# for loop

print("Numbers from 1 to 5")
for i in range(1, 6):
    print(i)

# while loop

print ("\nWhile Loop")
count = 1
while count <= 5:
    print(count)
    count += 1

# Break statement

print("\nBreak Statement")
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# Continue statement

print("\nContinue Statement")
for i in range(1, 11):
    if i == 6:
        continue
    print(i)

# Multiplication Table 
number = int(input("Enter a number:"))
print("\nMultiplication Table of", number)
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")