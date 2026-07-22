# Tuples in Python
    # Tuple of student grades (immutable)
students_grades_tuple = (8.5, 9.0, 7.8, 9.2, 8.8)
print(students_grades_tuple)

    # General tuple
mixed_tuple = (10, 15.5, "Alice", True, (1, 2, 3))
print(mixed_tuple)

    #operations with tuples
total_grades = sum(students_grades_tuple)
max_grade = max(students_grades_tuple)
min_grade = min(students_grades_tuple)
eight_point_five_count = students_grades_tuple.count(8.5)
print("Maximum grade:", max_grade)
print("Minimum grade:", min_grade) 
print("Total of grades:", total_grades)
print("Count of 8.5 grades:", eight_point_five_count)

average_grade = total_grades / len(students_grades_tuple)
print("Average grade:", average_grade)

    #sorting and reversing tuples
sorted_grades = tuple(sorted(students_grades_tuple))  # Sorting the tuple
reversed_grades = tuple(reversed(students_grades_tuple))  # Reversing the tuple
print("Sorted grades tuple:", sorted_grades)
print("Reversed grades tuple:", reversed_grades)

    #CRUD operations with tuples
# Note: Tuples are immutable, so we cannot add, remove, or modify elements directly like lists.
# However, we can create a new tuple based on existing ones.
new_grades_tuple = students_grades_tuple + (9.5,)  # Adding a new grade by creating a new tuple
print("New grades tuple after addition:", new_grades_tuple)

    #Data type attributes and methods
print(dir(students_grades_tuple))  # Lists all attributes and methods of the tuple object
print(len(students_grades_tuple))   # Length of the tuple
print(type(students_grades_tuple))  # Type of the objectcol

    #Tuple and dictionary
        #Converting a tuple of key-value pairs into a dictionary
key_value_tuple = (("name", "Alice"), ("age", 21), ("grades", [8.5, 9.0, 7.8]))
student_dict = dict(key_value_tuple)

print("Dictionary from tuple:", student_dict)
print(type(student_dict))  # Output: <class 'dict'>
print(student_dict["name"])  # Accessing value by key

student_dict["age"] = 22    # Modifying value by key
print("Updated age:", student_dict["age"]) # output: 22

student_dict["major"] = "Computer Science"  # Adding a new key-value pair
print("Added major:", student_dict["major"]) # output: Computer Science

    # Converting a dictionary back to a tuple of key-value pairs
dict_to_tuple = tuple(student_dict.items()) # Converts dictionary items to a tuple of key-value pairs
print("Tuple from dictionary:", dict_to_tuple)
print(type(dict_to_tuple))  # Output: <class 'tuple'>   

    #Conbinating tuples, lists and dictionaries
students_grades = [8.5, 9.0, 7.8, 9.2, 8.8]
combined = students_grades_tuple + tuple(students_grades)  # Combining a tuple and a list (converted to tuple)

print("Combined tuple and list:", combined)
print(type(combined))  # Output: <class 'tuple'>

student_info = {
    "name": "Alice",
    "age": 21,
    "grades": students_grades_tuple
}
combined_info = (student_info,) + students_grades_tuple  # Combining a dictionary (as a single-element tuple) and a tuple
print("Combined tuple and dictionary:", combined_info)
print(type(combined_info))  # Output: <class 'tuple'>