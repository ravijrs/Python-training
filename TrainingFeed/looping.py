""" 
take 5 inputs from user
after each input, print if input length is below or equal to 5, else print invalid
"""
for num in range(1, 6):
    name = input(f"Enter Input-{num} :")
    if len(name) <= 5:
        print(f"Output: {name}")
    else:
        break


for i in range(5):
    data = int(input("Enter Number: "))
    if data <= 100:
        print("Valid Input")
else:
    print("Invalid")

# while loop
name = "python"
current = 0
while current < len(name):
    print(name[current], current)
    current += 1
print("===================================")
name = "python"
current = len(name)-1
while current >= 0:
    print(name[current], current)
    current -= 1

# for-else
for i in range(5):
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
else:
    print("No Negative values Entered")

print("============================================")

# while-else
start = 0
while start < 5:
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
    start += 1
else:
    print("No Negative values Entered")