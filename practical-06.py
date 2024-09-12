# PRACTICAL-6 - PROGRAMS ON SET

# Program to create a Set and access its elements
fruits = {'apple', 'banana', 'cherry', 'date'}

# ACCESSING ELEMENTS
for fruit in fruits:
  print(fruit)

# ------------------------------------

# Program to modify a Set
fruits = {'apple', 'banana', 'cherry', 'date'}

# Adding an element
fruits.add('orange')

# Removing an element
fruits.remove('banana')

# Checking if an element exists
print('cherry' in fruits)

# Printing the modified Set
print('Modified Set', fruits)

# ------------------------------------

# Program to perform Set operations
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# Union of Sets
union = A | B
print("Union of A & B:", union)

# Intersection of Sets
intersection = A & B
print("Intersection of A & B:", intersection)

# Difference of Sets
difference = A - B
print("Difference of A & B:", difference)

# ------------------------------------

# Program to create a new Set using Set Comprehension
numbers = {1, 2, 3, 4, 5}

squared_set = {num**2 for num in numbers}
print("Squared Set", squared_set)