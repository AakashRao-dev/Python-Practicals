# ACCESSING AN ELEMENT IN TUPLE
fruits = ("apple", "cherry", "banana", "grapes")
print("fruit on position is:0", fruits[0])

print(fruits[1:3])


person = ("Aakash", 20, 'Technical Writer')
name, age, profession = person

print(f'Name: {name}')
print(f'Name: {age}')
print(f'Name: {profession}')


# COMBINING TWO TUPLES
combined_tuples = fruits + person
print(combined_tuples)

# FINDING ELEMENTS IN TUPLE
searched_fruit = "Mango"

print("The original tuple : " + str(combined_tuples))

# Check if element is present in tuple Using in operator
res = searched_fruit in combined_tuples

print("Does tuple contain required value ? : " + str(res))

# FINDING AND INDEXING IN TUPLES
count = fruits.count('apple')
index = fruits.index('grapes')

print(f'count of apple: {count}')
print(f'index of grapes: {index}')



# CREATING AND ACCESSING DICTIONARIES
student = {
    "name": "Aakash Rao",
    "age": 20,
    "profession": "Technical Writer"
}

print(student["name"])
print(student["age"])
print(student["profession"])

# MODIFYING DICTIONARIES

# updating value of an element
student["profession"] = "Software Enginner"

# deleting an element
del student["age"]

# adding a new element
student['roll no'] = 'empty'
print("Modified Dict", student)


# ITERATING OVER DICT ELEMENTS

for key, value in student.items():
    print(f'{key}, {value}')

# DICTIONARY COMPREHENSION

# Define the range of numbers
start = 1
end = 10

# Create the dictionary using dictionary comprehension
squares_dict = {num: num**2 for num in range(start, end + 1)}

# Print the dictionary
print(squares_dict)
