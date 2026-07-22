# Lists in Python
    # Lists of student grades    
students_grades = [8.5, 9.0, 7.8, 9.2, 8.8]
print(students_grades)

    # General list
mixed_list = [10, 15.5, "Alice", True, [1, 2, 3]]
print(mixed_list)

    #operations with lists
total_grades = sum(students_grades)
max_grade = max(students_grades)
min_grade = min(students_grades)
eight_point_five_count = students_grades.count(8.5)

print("Maximum grade:", max_grade)
print("Minimum grade:", min_grade)  
print("Total of grades:", total_grades)
print("Count of 8.5 grades:", eight_point_five_count)

average_grade = total_grades / len(students_grades)
print("Average grade:", average_grade)

print(mixed_list * 2)  # Repeats the list twice
print(mixed_list + students_grades)  # Concatenates two lists

    #range of lists
numbers = list(range(1, 11))  # List of numbers from 1 to 10
print(numbers)

other_numbers = list(range(1, 9, 2)) # output: [1, 3, 5, 7]
other_numbers_2 = list(range(0, 21, 5)) # Output: [0, 5, 10, 15, 20]
print(other_numbers)

    #Data type attributes and methods
print(dir(students_grades))  # Lists all attributes and methods of the list object
print(len(students_grades))   # Length of the list
print(type(students_grades))  # Type of the object

    # Conveting
        # From list to tuple
grades_tuple = tuple(students_grades)
print("Tuple from list:", grades_tuple)
print(type(grades_tuple))  # Output: <class 'tuple'>

        # From string to list
name_str = "John Doe"
name_list = name_str.split()  # Splits the string into a list of words
other_name_list = list(name_str)  # Converts the string into a list of characters
print("List from string:", name_list)
print("List of characters from string:", other_name_list)

        # From list to string
joined_name_str = str.join(name_list)  # Joins the list of words into a single string
hyphen_joined_str = "-".join(name_list)  # Joins the list of words with hyphens
print("Joined string from list:", joined_name_str)
print("Hyphen joined string from list:", hyphen_joined_str)

        # From tuple to list
tuple_to_list = list(grades_tuple)
print("List from tuple:", tuple_to_list)
print(type(tuple_to_list))  # Output: <class 'list'>

    # CRUD operations with lists
        # Accessing elements by index, portioning, and negative indexing
first_grade = students_grades[0]
print("First grade:", first_grade)

last_grade = students_grades[-1]
print("Last grade:", last_grade)

slice_grades = students_grades[1:4]  # Grades from index 1 to 3
print("Grades from index 1 to 3:", slice_grades)
slice_from_start = students_grades[:3]  # First three grades
print("First three grades:", slice_from_start)
slice_to_end = students_grades[2:]  # From index 2 to the end
print("Grades from index 2 to end:", slice_to_end)
slice_full = students_grades[:]  # Full list copy
print("Full list copy:", slice_full)
slice_negative = students_grades[-4:-1]  # From the fourth last to the second last, output: [9.0, 7.8, 9.2]
print("Grades from -4 to -1:", slice_negative)
slice_negative_to_end = students_grades[-3:]  # Last three grades
print("Last three grades:", slice_negative_to_end)
slice_negative_from_start = students_grades[:-2]  # All but the last two grades
print("All but last two grades:", slice_negative_from_start)

letter_str_list = mixed_list[2][3]   # Accessing 'c' from "Alice"
print("Accessed character from string in list:", letter_str_list)

        # Modifying elements
old_student_grade = students_grades[2]
students_grades[2] = 8.0    
print("Updated grades:", old_student_grade, "->", students_grades[2])

        # Adding elements
students_grades.append(9.5)  # Adds 9.5 at the end
students_grades.insert(1, 8.7)  # Inserts 8.7 at index 1

print("Grades after additions:", students_grades)

        # Removing elements
removed_grade = students_grades.pop()  # Removes and returns the last element
students_grades.remove(8.7)  # Removes the first occurrence of 8.7

print("Grades after removals:", students_grades)
print("Removed last grade:", removed_grade)

    #slicing lists
first_three_grades = students_grades[0:3]  
print("First three grades:", first_three_grades)

last_two_grades = students_grades[-2:]  # Last two grades
print("Last two grades:", last_two_grades)

middle_grades = students_grades[1:4]  # Grades from index 1 to 3
print("Middle grades (index 1 to 3):", middle_grades)

all_but_first = students_grades[1:]  # All but the first grade
print("All but first grade:", all_but_first)

all_but_last = students_grades[:-1]  # All but the last grade
print("All but last grade:", all_but_last)

    #sorting and reversing lists
students_grades.sort()  # Sorts the list in ascending order
students_grades.reverse()  # Reverses the list