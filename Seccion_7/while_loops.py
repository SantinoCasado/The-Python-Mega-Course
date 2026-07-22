# While loops
a = 3
while a > 0:
    print(a)
    # up to here is an infinite loop
    a -= 1  # Decrement a by 1 to prevent infinite loop


# While loop with else
b = 3
while b > 0:
    print(b)
    b -= 1
else:
    print("Loop finished") # This will execute when the loop condition is no longer true

# While loop with break
c = 3
while c > 0:
    print(c)
    if c == 2:  # When c is 2, exit the loop
        break
    c -= 1

# While loop with continue
d = 3
while d > 0:
    d -= 1
    if d == 2:  # When d is 2, skip the rest of the loop and go to the next iteration
        continue
    print(d)

# Loop through a string
text = "hello"
while text:
    print(text[0])  # Print the first character
    text = text[1:]  # Remove the first character

# Loop through a dictionary
contacts = {"Alice": 123, "Bob": 456, "Charlie": 789}
while contacts:
    name, phone = contacts.popitem()  # Get a key-value pair
    print(f"Name: {name}, Phone: {phone}")

# Loop through a list with index
colors = ["red", "green", "blue"]
while colors:
    print(colors[0])  # Print the first color
    colors = colors[1:]  # Remove the first color

# While loop with a counter
count = 0
while count < 5:
    print(count)
    count += 1
print("Final count:", count)  # Output: Final count: 5

# Loop through a set
unique_numbers = {1, 2, 3, 4, 5}
while unique_numbers:
    print(unique_numbers.pop())  # Print and remove an element from the set

# Loop through a list with condition
colors = [11, 34, 98, 43, 45, 54, 54]
while colors:
    item = colors.pop(0)  # Get the first item
    if item > 50:
        print(item)

# Loop through a list with type checking
colors = [11, 34, 98, 43, 45, 54, 54]
while colors:
    item = colors.pop(0)  # Get the first item
    if isinstance(item, int):
        print(item)

# Loop with flags
running = True
count = 0
while running:
    print(count)
    count += 1
    if count == 5:
        running = False

# Validation loop
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter something (type 'exit' to quit): ")
    print("You entered:", user_input)
print("Exited the loop.")

# Validation type loop
intNumber = None
string = ""
floatNumber = None
booleanValue = None
flag = True

while True:
    # Validar entero
    while True:
        intNumber = input("Enter an integer: ")
        if intNumber.isdigit():
            intNumber = int(intNumber)
            break
        else:
            print("That's not a valid integer. Please try again.")
            continue

    # Validar string
    while True:
        string = input("Enter a string: ")
        if string.isalpha():
            break
        else:
            print("That's not a valid string. Please try again.")
            continue

    # Validar float
    while True:
        floatNumber = input("Enter a float: ")
        try:
            floatNumber = float(floatNumber)
            break
        except ValueError:
            print("That's not a valid float. Please try again.")
            continue

    # Validar booleano
    while True:
        booleanValue = input("Enter a boolean (True/False): ")
        if booleanValue.lower() in ["true", "false"]:
            booleanValue = booleanValue.lower() == "true"
            break
        else:
            print("That's not a valid boolean. Please try again.")
            continue

    flag = False

# Nested while loop
i = 1
while i <= 3:          # Outer loop
    j = 1
    while j <= 2:      # Inner loop
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1

# Loop through a list and modify elements
numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    numbers[index] *= 2  # Double each element
    index += 1
print(numbers)  # Output: [2, 4, 6, 8, 10]
