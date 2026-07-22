# Functions in Python

#Structure of a function
def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean
print("Mean of students_grades:", mean([8.5, 9.0, 7.8, 9.2, 8.8]))  # Output: 8.86

#Function with multiple parameters
def greet(name, message):
    return f"Hello {name}, {message}"
print(greet("you", "welcome to the Python course!"))  # Output: Hello you, welcome to the Python course!

#Function with default parameter
def greet(name, message="welcome to the Python course!"):
    return f"Hello {name}, {message}"
print(greet("you"))  # Output: Hello you, welcome to the Python course!

#Function with variable number of arguments
def average(*args):     # Accepts a variable number of arguments (list, tuple, etc.)
    return sum(args) / len(args)
print("Average of 3, 4, 5:", average(3, 4, 5))  # Output: 4.0
print("Average of 10, 20, 30, 40:", average(10, 20, 30, 40))  # Output: 25.0

"""
Define a function that takes an indefinite number of strings as parameters and returns a 
list containing all the strings in UPPERCASE and sorted alphabetically. 
For example, if I called your function with foo("snow", "glacier", "iceberg") 
it should return ["GLACIER", "ICEBERG", "SNOW"].
"""

def upperStr(*args):
    return sorted([i.upper() for i in args])
    
print(upperStr("snow", "glacier", "iceberg"))
print(upperStr("bbb", "ccc", "aaa"))
#------------------------------------------- PREVIOUS EXAMPLES ---------------------------------------------------------------------------------------#
#Function with keyword arguments
def mean(**kwargs): # kwargs is a dictionary (it only accepts key=value pairs, not positional arguments)
    return sum(kwargs.values()) / len(kwargs) # Calculate the mean of the values in the dictionary

print("Mean of a=8, b=9, c=7:", mean(a=8, b=9, c=7))  # Output: 8.0

    #Other example
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."
print(describe_person(age=30, city="New York", name="Alice"))  # Output: Alice is 30 years old and lives in New York.

#Function with return statement
def square(number):
    return number * number
print("Square of 5:", square(5))  # Output: 25

#Function without return statement (returns None)
def print_square(number):
    print(number * number) 

print("Print square of 5:")
print_square(5)  # Output: 25

#Function with docstring
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b
print("Multiply 4 and 5:", multiply(4, 5))  # Output: 20
print("Docstring of multiply function:", multiply.__doc__)  # Output: Returns the product of a and b.

"Hola".u