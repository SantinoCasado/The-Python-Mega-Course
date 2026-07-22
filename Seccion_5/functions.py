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
