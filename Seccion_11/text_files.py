# Text files in Python

"""
File modes summary
'r' - Read mode (default, you can only read the file)
'w' - Write mode (you can write to the file, if the file exists it will overwrite it)
'a' - Append mode (you can add content to the end of the file)
'r+' - Read and write mode (you can read and write to the file)
'w+' - Write and read mode (you can write and read to the file, if the file exists it will overwrite it)
'a+' - Append and read mode (you can add content to the end of the file and read it)
'b' - Binary mode (used for non-text files like images, you can combine it with other modes, e.g., 'rb', 'wb')
't' - Text mode (default, you can combine it with other modes, e.g., 'rt', 'wt')  # Not necessary to specify 't' as it is the default mode
'x' - Exclusive creation mode (creates a new file, returns an error if the file already exists)
'x+' - Exclusive creation and read mode (creates a new file and allows reading, returns an error if the file already exists)  # Not commonly used
'U' - Universal newline mode (deprecated, use 'r' mode instead, it allows reading files with different newline conventions)   # Not commonly used
'U+' - Universal newline and read mode (deprecated, use 'r+' mode instead)  # Not commonly used
Note: You can combine modes, e.g., 'rb' for reading a binary file, 'w+' for writing and reading a file, etc.
"""

my_file = open("fruits.txt") # Open the file in read mode by default
print(my_file.read()) # Read the entire file content
my_file.close() # Close the file

# others ways to open a file
my_file = open("fruits.txt", "r") # Read mode (default, you can only read the file)
print(my_file.read())
my_file.close()

my_file = open("vegetables.txt", "w") # Write mode (you can write to the file, if the file exists it will overwrite it)
my_file.write("Carrot\nBroccoli\nSpinach\n") # Write to the file
my_file.close() # Close the file

my_file = open("fruits.txt", "a") # Append mode (you can add content to the end of the file)
my_file.write("Orange\n") # Add a new line to the file
my_file.close() # Close the file

# READ and WRITE mode
my_file = open("vegetables.txt ", "r+") # Read and write mode (you can read and write to the file)
print(my_file.read()) # Read the entire file content
my_file.write("Mango\n") # Write to the file
my_file.close() # Close the file

# Context manager (with statement) - automatically closes the file
with open("fruits.txt", "r") as my_file:
    content = my_file.read()
    print(content)
    # Not necessary when using 'with' statement, but included for clarity

    # WITH statement with readlines()
with open("fruits.txt", "r") as my_file:
    lines = my_file.readlines() # Read all lines into a list
    print(lines) # Output: ['Apple\n', 'Banana\n', 'Cherry\n', 'Orange\n', 'Mango\n']
    for line in lines:
        print(line.strip()) # Print each line without extra whitespace
    # Output:
    # Apple
    # Banana
    # Cherry
    # Orange
    # Mango

    # Writing multiple lines
with open("vegetables.txt", "w") as my_file:
    my_file.writelines(["Carrot\n", "Broccoli\n", "Spinach\n"]) # Write multiple lines to the file
    # Note: writelines() does not add newline characters, so we need to include them in the strings

    # Writing individual lines
with open("vegetables.txt", "w") as my_file:
    my_file.write("Carrot\n")
    my_file.write("Broccoli\n")
    my_file.write("Spinach\n")
    # Each write() call adds a newline character at the end of the string

# File cursor methods
my_file = open("fruits.txt", "r")
print(my_file.read())
print(my_file.read()) # It would print at the end of the file, so nothing is printed

    # With seek() method we can move the cursor to a specific position
my_file.seek(0) # Move the cursor to the beginning of the file
print(my_file.read())   # Now it prints the entire file content again
my_file.seek(7) # Move the cursor to the 7th byte (character)
print(my_file.read())   # Now it prints from the 7th byte to the end, output: Banana\nCherry\nOrange\n
my_file.close()

    # With tell() method we can know the current position of the cursor
my_file = open("fruits.txt", "r")
print(my_file.tell()) # Print the current cursor position
my_file.seek(0) # Move the cursor to the beginning of the file
print(my_file.tell()) # Print the current cursor position
my_file.close()

    # Reading a specific number of characters
my_file = open("fruits.txt", "r")
print(my_file.read(5)) # Read the first 5 characters
my_file.close()

    # Reading files line by line
my_file = open("fruits.txt", "r")
for line in my_file:
    print(line.strip()) # Print each line without extra whitespace
my_file.close()

# Reading all lines into a list
my_file = open("fruits.txt", "r")
fruits = my_file.readlines()
my_file.close()

print(fruits) # Output: ['Apple\n', 'Banana\n', 'Cherry\n', 'Orange\n', 'Mango\n']
print([fruit.strip() for fruit in fruits]) # Print each fruit without extra whitespace


# Path files
#With out "with" statement
path = "Files\\file.txt"  # Use double backslashes or raw string to avoid escape characters
my_file = open(path)  # Use forward slashes or double backslashes
print(my_file.read())
my_file.close()

my_file = open("Files/file.txt")  # Use forward slashes or double backslashes
print(my_file.read())
my_file.close()

# With "with" statement
with open("Files/file.txt") as my_file:  # Use forward slashes or double backslashes
    print(my_file.read())

with open("Files\\file.txt") as my_file:  # Use forward slashes or double backslashes
    print(my_file.read())

with open(r"Files\file.txt") as my_file:  # Use raw string to avoid escape characters
    print(my_file.read())


"""
Read the bear.txt file, and print out the first 90 characters of its content.
"""
with open("Files/bear.txt", "r") as my_file:
    content = my_file.read(90)
    print(content)

"""
Define a function that gets a single string character and a 
filepath as parameters and returns the number of occurences of that character in the file.
"""
def count_character_in_file(char, filepath):
    with open(filepath, "r") as my_file:
        content = my_file.read()
        return content.count(char)

"""
Create a first.txt file that contains the first 90 characters of bear.txt.

Note that you should read the content of bear.txt with Python, extract its 
first 90 characters with Python, and write those characters in first.txt with Python.
"""
with open("first.txt", "w") as file:
    with open("bear.txt", "r") as file_1:
        bearFile = file_1.read((90))
    
    file.write(bearFile)

# Cursor methods summary
    # seek(offset, whence) - Move the cursor to a specific position in the file
with open("fruits.txt", "r") as my_file:
    print(my_file.read(5))  # Read the first 5 characters
    my_file.seek(0)          # Move the cursor to the beginning of the file
    print(my_file.read(5))  # Read the first 5 characters again
    my_file.seek(10)         # Move the cursor to the 10th byte (character)
    print(my_file.read(5))  # Read 5 characters from the 10th byte
    #Now you wanto to print the last 5 characters of the file
    my_file.seek(0, 2)      # Move the cursor to the end of the file, 2 means from the end and 0 means no offset
    end_position = my_file.tell()  # Get the current position (end of file)

    # offset - Number of bytes to move the cursor
    my_file.seek(end_position - 5, 0)  # Move the cursor to the last 5 bytes
    print(my_file.read(5))  # Read the last 5 bytes

# whence - Reference point for the offset (0: beginning, 1: current position, 2: end)   # Default is 0 (beginning of the file)
# tell() - Return the current position of the cursor in the file
# read(size) - Read a specific number of characters from the file
# readline() - Read a single line from the file
# readlines() - Read all lines from the file and return them as a list
# write(string) - Write a string to the file
# writelines(list_of_strings) - Write a list of strings to the file


"""
Append the text of bear1.txt to bear2.txt. 
In other words, bear2.txt should contain its 
text and the text of bear1.txt after that.
"""
with open("bear2.txt", "a") as file_2:
    with open("bear1.txt", "r") as file_1:
        file_2.write(file_1.read())

"""
The existing content of data.txt looks like this:
1.3, 1.5
2.3, 2.7
Use Python to modify the content of data.txt so that its content looks like below:
1.3, 1.5
2.3, 2.7
1.3, 1.5
2.3, 2.7
1.3, 1.5
2.3, 2.7
So, you need to find a way to insert the existing content two more times.
"""
with open("data.txt", "a+") as file:
    file.seek(0)  # Mueve el cursor al inicio para leer todo el contenido
    content = file.read()
    file.write(content * 2)