def weather_condition(temp):
    if temp > 30:
        return "It's a hot day"
    elif temp > 20:
        return "It's a nice day"
    elif temp > 10:
        return "It's a bit cold"
    else:
        return "It's cold"
    
input_temp = float(input("Enter the temperature: "))
print(weather_condition(input_temp))

# INPUTS
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input string to integer
height = float(input("Enter your height in meters: "))  # Convert input string to float
is_student = input("Are you a student? (yes/no): ").strip().lower() == 'yes'  # Convert to boolean, yes/no to True/False

print(f"Name: {name}, Age: {age}, Height: {height}m, Is Student: {is_student}")

# String formatting
user_input = input("Enter your name: ")

    # Old style formatting
message = "hello %s" % user_input   # %s es un marcador de posición para una cadena, y el operador % inserta el valor de user_input en ese lugar.
print(message)  # Output: hello <user_input>

    # New style 
message = f"hello {user_input}"
print(message)  # Output: hello <user_input>
    
    # Using format() method
message = "hello {}".format(user_input)
print(message)  # Output: hello <user_input>

    #Multiple forrmatting
message = "Hello %s, you are %d years old and your height is %.2f meters." % (user_input, age, height)
print(message)  # Output: Hello <user_input>, you are <age> years old and your height is <height> meters.

message = f"Hello {user_input}, you are {age} years old and your height is {height} meters."
print(message)  # Output: Hello <user_input>, you are <age> years old and your height is <height> meters.

# String methods with user input
user_input = input("Enter a string: ")
print("Uppercase:", user_input.upper()) # Output: Uppercase version of the input
print("Lowercase:", user_input.lower()) # Output: Lowercase version of the input
print("Stripped:", user_input.strip())   # Output: Input string without leading/trailing whitespace
print("Title case:", user_input.title())  # Output: Title-cased version of the input
print("Reversed:", user_input[::-1])      # Output: Reversed version of the input

# Multiple variable input
x, y = map(int, input("Enter two integers separated by space: ").split())   # Splits input string and converts to integers
print("X:", x)
print("Y:", y) 
print("Sum:", x + y)