#Dicctionaries
student = {
    "name": "Alice",
    "age": 21,
    "grades": [8.5, 9.0, 7.8]
}

students_grades_dict = {
    "Alice": [8.5, 9.0, 7.8],
    "Bob": [9.2, 8.8, 8.0],
    "Charlie": [7.5, 8.0, 9.0]
}

print(students_grades_dict)
print(student)

print(student["name"])  # Accessing value by key
student["age"] = 22    # Modifying value by key
print("Updated age:", student["age"]) # output: 22

student["major"] = "Computer Science"  # Adding a new key-value pair
print("Added major:", student["major"]) # output: Computer Science

    # Dictionary methods and attributes
print(student.keys())    # Output: dict_keys(['name', 'age', 'grades', 'major'])
print(student.values())  # Output: dict_values(['Alice', 22, [8.5, 9.0, 7.8], 'Computer Science'])
print(student.items())   # Output: dict_items([('name', 'Alice'), ('age', 22), ('grades', [8.5, 9.0, 7.8]), ('major', 'Computer Science')])

    # Dictionary properties
print(len(student))      # Output: 4
print(type(student))     # Output: <class 'dict'>
print(dir(student))      # Lists all attributes and methods of the dict object

    #operations with dictionaries
student_copy = student.copy()  # Creating a shallow copy of the dictionary

students_grades_sum = sum(students_grades_dict.values())  # Summing the grades list
students_len = len(students_grades_dict)  # Counting the number of students
students_average = students_grades_sum / students_len  # Calculating the average grades
print("Students grades sum:", students_grades_sum)
print("Number of students:", students_len)
print("Students average grade:", students_average)

    #sorting and reversing dictionaries
sorted_by_keys = dict(sorted(student.items()))  # Sorting the dictionary by keys
sorted_by_values = dict(sorted(student.items(), key=lambda item: item[1]))  # Sorting by values
print("Sorted by keys:", sorted_by_keys)
print("Sorted by values:", sorted_by_values)

    #CRUD operations with dictionaries
student_update = {
    "name": "Alice",
    "age": 22,
    "grades": [8.5, 9.0, 7.8]
}
        #Read
print("Original student:", student_update)
            #Accessing value by key
print("Name:", student_update["name"])
print("Age:", student_update["age"])
print("Grades:", student_update["grades"])

            #Accesing by slicing
slice_grades = student_update["grades"][0:2]  # Slicing grades from index 0 to 1
print("Sliced grades (0 to 1):", slice_grades)
slice_from_start = student_update["grades"][:2]  # Slicing from start to index 1
print("Sliced grades (start to 1):", slice_from_start)
slice_to_end = student_update["grades"][1:]  # Slicing from index 1 to end
print("Sliced grades (1 to end):", slice_to_end)
slice_full = student_update["grades"][:]  # Full grades copy
print("Full grades copy:", slice_full)
slice_negative = student_update["grades"][-2:]  # Last two grades
print("Last two grades:", slice_negative)
slice_negative_from_start = student_update["grades"][:-1]  # All but the last grade
print("All but last grade:", slice_negative_from_start)

            #Accesing a character from a string in the dictionary
first_letter_name = student_update["name"][0]  # Accessing first character of the name
print("First letter of name:", first_letter_name)

        #Update
student_update["age"] = 23  # Update age
print("Updated age:", student_update["age"])

        #Add
student_update["major"] = "Computer Science"  # Add major
print("Added major:", student_update["major"])

        #Delete 
del student_update["grades"]  # Remove grades
print("Removed grades:", student_update["grades"])

print("Updated student:", student_update)


    # More dictionary operations
print(student.get("name"))  # Accessing value by key using get method
print(student.get("graduation_year", "Not specified"))  # Accessing non-existing key with default value, output: Not specified
print("age" in student)  # Checking if key exists, output: True
print("graduation_year" in student)  # Checking if key exists, output: False
print(student.pop("major", "Key not found"))  # Removing a key-value pair, output: Computer Science