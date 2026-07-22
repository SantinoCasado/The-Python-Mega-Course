# For loop
monday_temperatures = [9.1, 8.8, 7.5]

    # For each element in the list, do something
for temp in monday_temperatures:
    print(temp)

    # For loop with range
for i in range(10):  # From 0 to 9
    print(i)

    # For loop with range and step
for i in range(1, 10, 2):  # From 1 to 9, step 2
    print(i)

    # For loop with range and custom start and end
for i in range(5, 15):  # From 5 to 14
    print(i)

    # For with len()
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])

    # For loop with else
for i in range(5):
    print(i)
else:
    print("Loop finished")

    # For loop with continue
for i in range(5):
    if i == 2:      # When i is 2, skip the rest of the loop and go to the next iteration
        continue
    print(i)

    # For loop with break
for i in range(5):
    if i == 2:      # When i is 2, exit the loop
        break
    print(i)

    # Nested for loop
for i in range(3):          # Outer loop
    for j in range(2):      # Inner loop
        print(f"i: {i}, j: {j}")

    # Loop through a string
for char in "hello":
    print(char)

    # Loop through a counter
count = 0
for i in range(5):
    count += 1
print(count)  # Output: 5

    # Loop through a list with index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

    # Loop through a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(key, value)

        #Other form
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}

for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")   # pair[0] is the key, pair[1] is the value

    # Loop through a set
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)

    # Loop through a tuple
coordinates = (10, 20)
for coord in coordinates:
    print(coord)

# Matrix (list of lists)

    # Columns and rows with for loop
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matrix[0])):  # Iterate over columns
    for j in range(len(matrix)):  # Iterate over rows
        print(matrix[j][i])


# List comprehension
squares = [x**2 for x in range(10)]  # List of squares from 0 to 9
print(squares)