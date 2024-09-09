# PRACTICAL-5

# Program to create a dictionary and access its elements
student = {"name": "Aakash", "roll_number": 101, "marks": 35}

# Accessing elements
print("Student Name:", student["name"])
print("Roll Number:", student["roll_number"])
print("Marks:", student["marks"])


# Program to modify a dictionary
student = {"name": "Aakash", "roll_number": 101, "marks": 35}
student["marks"] = 98 # updating the value
student["grade"] = "A" # Adding a new key-value pair
del student["roll_number"] # deleing a key-value pair
print("Modified Student:", student)


# Program to iterate over a dictionary
student = {"name": "Aakash", "roll_number": 101, "marks": 95}
for key, value in student.items():
  print(f"{key}: {value}")


# Program to check if a key exists in a dictioanry
student = {"name": "Aakash", "roll_number": 101, "marks": 95}
search_key = "grade"

if search_key in student:
  print(f"{search_key} exists in the dictionary")
else:
  print(f"{search_key} does not exist in the dictionary")


# Program to create a dictionary using dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = {num: num**2 for num in numbers}
print("Squared Numbers:", squared_numbers)