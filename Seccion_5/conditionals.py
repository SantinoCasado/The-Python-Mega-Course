#Conditionals
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

grade = 85
if grade >= 90: 
    print("You got an A.")
else:
    print("You did not get an A.")

#Conditionals operators
temperature = 25
    #Mayor than
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")

    #Less than
if temperature < 15:
    print("It's a cold day.")
else:
    print("It's not a cold day.")

    #Greater than or equal to
if temperature >= 25:
    print("It's warm.")
else:
    print("It's not warm.")

    #Less than or equal to
if temperature <= 20:
    print("It's cool.")
else:
    print("It's not cool.")

    #Equal to
if temperature == 25:
    print("The temperature is exactly 25 degrees.")
else:
    print("The temperature is not 25 degrees.")

    #Not equal to
if temperature != 25:
    print("The temperature is not 25 degrees.")
else:
    print("The temperature is exactly 25 degrees.")

# Diferents methods to evaluate conditions
str_question = input("Enter a question: ").strip().lower()  # Get user input, remove leading/trailing whitespace, and convert to lowercase
if str_question.startswith(("how", "why", "what")):  # Check if the string starts with "how", "why", or "what"
    str_question = (str_question + "?").capitalize()
    print(str_question)  # Output: How is the day?
else:
    print((str_question + ".").capitalize())  # Output: How is the day.

#Multiple conditions
time = 14  # 2 PM
if time < 12:
    print("Good morning!")
elif time < 18:
    print("Good afternoon!")
else:
    print("Good evening!")

#Logical operators
is_raining = True
is_sunny = False

    #Using 'and' operator
if is_raining and is_sunny:
    print("It's raining and sunny.")
elif is_raining and not is_sunny:   # and not operator, negation
    print("It's raining but not sunny.")
elif not is_raining and is_sunny:   # not operator, negation
    print("It's sunny but not raining.")
else:
    print("It's neither raining nor sunny.")

    #Using 'or' operator
if is_raining or is_sunny:      #True if at least one condition is true
    print("It's either raining or sunny.")
else:
    print("It's neither raining nor sunny.")

#Multiple conditions with 'and' and 'or'
hour = 10  # 10 AM
if (hour < 12 and is_sunny) or (hour >= 12 and not is_sunny):   #True if at least one condition is true
    print("Good morning! It's a sunny morning.")
else:
    print("Good afternoon or it's not sunny.")

#Nested conditionals
day = "Saturday"
if day == "Saturday":
    print("It's the weekend!")
    if is_sunny:  # Nested if
        print("It's a sunny Saturday!")
    else:
        print("It's a cloudy Saturday.")

#Match-case statement
day_of_week = 3
match day_of_week:
    case 1:
        print("It's Monday.")
    case 2:
        print("It's Tuesday.")
    case 3:
        print("It's Wednesday.")
    case 4:
        print("It's Thursday.")
    case 5:
        print("It's Friday.")
    case 6:
        print("It's Saturday.")
    case 7:
        print("It's Sunday.")
    case _:  # Default case
        print("Invalid day of the week.")

    # Match-case with multiple conditions
fruit = "apple"
match fruit:
    case "apple":
        if is_raining:  # Nested if
            print("It's an apple and it's raining.")
        print("It's an apple.")
    case _:
        print("Unknown fruit.")

# Type instance checking with conditionals
value = 10.5
if isinstance(value, int):
    print("The value is an integer.")
elif isinstance(value, float):
    print("The value is a float.")
elif isinstance(value, str):
    print("The value is a string.")
else:
    print("The value is of an unknown type.")

    # Type checking with conditionals
if isinstance(value, int):
    print("The value is an integer.")
elif isinstance(value, float):
    print("The value is a float.")
elif isinstance(value, str):
    print("The value is a string.")
else:
    print("The value is of an unknown type.")

#List membership
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list of fruits.")
if "grape" not in fruits:
    print("Grape is not in the list of fruits.")
if "apple" in fruits and "cherry" in fruits:
    print("Both apple and cherry are in the list of fruits.")

    #Using 'and' and 'or' with membership
if "banana" in fruits or "grape" in fruits:
    print("At least one of banana or grape is in the list of fruits.")

    #Using 'and' and 'or' with membership and conditionals
if ("banana" in fruits and temperature > 20) or ("grape" in fruits and temperature <= 20):
    print("It's a warm day with banana or a cool day with grape.")

    #Using 'not' with membership
if "grape" not in fruits and not is_raining:
    print("It's not raining and grape is not in the list of fruits.")

#Dictionary membership
student = {"name": "Alice", "age": 20, "grade": "A"}

if "name" in student:
    print("The student's name is:", student["name"])
if "address" not in student:
    print("The student's address is not available.")
if "age" in student and student["age"] >= 18:
    print("The student is an adult.")

    #Using 'and' and 'or' with dictionary membership
if "grade" in student or "address" in student:
    print("The student has a grade or an address.")
if "grade" in student and student["grade"] == "A":
    print("The student has an A grade.")

    #Using 'not' with dictionary membership
if "address" not in student and not is_raining:
    print("It's not raining and the student's address is not available.")
if "name" in student and student["name"] == "Alice" and not is_raining:
    print("It's not raining and the student's name is Alice.")
