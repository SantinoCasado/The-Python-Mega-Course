temps = [221, 234, 340, 239]

# Convert to Celsius
new_temps = [temp / 10 for temp in temps]
print(new_temps)    # Output: [22.1, 23.4, 34.0, 23.9]


# Example with condition
other_temps = [221, -234, 340, -9999, 239, ]  # -9999 is an error value

new_temps = [temp / 10 for temp in other_temps if temp != -9999] # Filter out error values
print(new_temps)    # Output: [22.1, -23.4, 34.0, 23.9]


"""
Define a function that takes as a parameter a list that contains both integers and strings 
and returns the list containing only the integers. For example, 
if I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].
"""
def onlyInt(list):
    return [i for i in list if isinstance(i, int)]

print(onlyInt([99, 'no data', 95, 94, 'no data']))


"""
Define a function that takes as parameter list of numbers and returns the list containing 
only the numbers that are greater than 0. For example, I called your function 
with foo([-5, 3, -1, 101]) it should return [3, 101].
"""
def onlyGraterThan0 (list):
    return [i for i in list if i > 0]
    
print(onlyGraterThan0([-5, 3, -1, 101]))

# Syntax with else
other_temps1 = [221, -234, 340, -9999, 239, ]  # -9999 is an error value
    # You move the if condition before the for loop and add an else statement
new_temps1 = [temp / 10 if temp != -9999 else 0 for temp in other_temps1] # Replace error values with 0
print(new_temps1)   # Output: [22.1, -23.4, 34.0, 0, 23.9]

"""
Define a function that takes as parameter a list that contains both numbers and strings and 
returns the same list but with zeros instead of strings. For example, I called your function with 
foo([99, 'no data', 95, 94, 'no data']) it should return [99, 0, 95, 94, 0].
"""
def replaceStrWith0 (list):
    # Agrego el elemento si es int, sino agrego 0 en su lugar
    return [i if isinstance(i, int) else 0 for i in list]

print(replaceStrWith0([99, 'no data', 95, 94, 'no data']))

"""
Define a function that takes as parameter a list that contains decimal numbers as 
strings and returns the sum of those numbers. For example, 
I called your function with foo(['1.2', '2.6', '3.3']) it should return 7.1. 
Note that the floats of the input list are string datatypes.
"""
def sumOfStrFloat (list):
    return sum([float(i) for i in list])

print(sumOfStrFloat(['1.2', '2.6', '3.3']))


# Syntax with elif
other_temps2 = [221, -234, 340, -9999, 239, ]  # -9999 is an error value
    # if temp is not -9999, convert to Celsius; if temp is negative, set to 0; otherwise, keep the value
new_temps2 = [temp / 10 if temp != -9999 else 0 if temp < 0 else temp for temp in other_temps2]
print(new_temps2)   # Output: [22.1, 0, 34.0, 0, 23.9]

# Syntax with multiple for loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Flatten the matrix, the first for loop iterates through each row, and the second for loop iterates through each number in the row
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Flatten and convert to strings
flattened_str = [str(num) for row in matrix for num in row]
print(flattened_str)  # Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9']
