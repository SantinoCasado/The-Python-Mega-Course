#Integers
x = 10
y = 5
sum_xy = x + y

print(sum_xy)

#Float
x_float = 10.5
y_float = 5.2  
sum_xy_float = x_float + y_float

print(sum_xy_float)

#Strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(full_name)

    #Accessing characters by index, slicing, and negative indexing
first_char = full_name[0]
print("First character:", first_char)

last_char = full_name[-1]
print("Last character:", last_char)

slice_name = full_name[0:4]  # Slicing from index 0 to 3, output: John
print("Sliced name (0 to 3):", slice_name)
slice_from_start = full_name[:4]  # Slicing from start to index 3, output: John
print("Sliced name (start to 3):", slice_from_start)
slice_to_end = full_name[5:]  # Slicing from index 5 to end, output: Doe
print("Sliced name (5 to end):", slice_to_end)
slice_full = full_name[:]  # Full string copy, output: John Doe
print("Full string copy:", slice_full)
slice_negative = full_name[-3:]  # Last three characters, output: oe
print("Last three characters:", slice_negative)
slice_negative_from_start = full_name[:-3]  # All but the last three characters, output: John D
print("All but last three characters:", slice_negative_from_start)

    # String methods
upper_str = full_name.upper()
print("Uppercase:", upper_str)  # Output: JOHN DOE
lower_str = full_name.lower()  
print("Lowercase:", lower_str)  # Output: john doe
strip_str = "   Hello World!   "
print("Stripped string:", strip_str.strip())  # Output: Hello World!


#Booleans
is_active = True
is_admin = False

print(is_active, is_admin)
print(is_active and is_admin)  # Output: False
print(is_active or is_admin)   # Output: True

#Data Types Summary
print(type(x))            # Output: <class 'int'>
print(type(x_float))      # Output: <class 'float'>
print(type(full_name))    # Output: <class 'str'>
print(type(is_active))     # Output: <class 'bool'>

#Type Conversion
num_str = "100"

num_int = int(num_str)
print(num_int + 50)  # Output: 150

num_float = float(num_str)
print(num_float + 50.5)  # Output: 150.5

num_str_converted = str(200)
print(num_str_converted + " is a string")  # Output: 200 is a string

lower_str = "hello"
upper_str = lower_str.upper()
print(upper_str)  # Output: HELLO

upper_str_converted = "WORLD"
lower_str_converted = upper_str_converted.lower()
print(lower_str_converted)  # Output: world

#Type Checking
print(isinstance(x, int))          # Output: True
print(isinstance(y, float))        # Output: False

print(isinstance(x_float, float))  # Output: True
print(isinstance(y_float, int))    # Output: False

print(isinstance(full_name, str))  # Output: True
print(isinstance(first_name, int)) # Output: False

print(isinstance(is_active, bool)) # Output: True
print(isinstance(is_admin, str))   # Output: False