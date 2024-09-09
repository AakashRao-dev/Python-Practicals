# PRACTICAL-4:

# Program to create a tuple and access its elements
fruits = ( "apple", "banana", "cherry", "date")

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slicing the tuple:", fruits[1:3])

# Program to demonstrate tuple packing and unpacking
person = ("John", 30, "Engineer")

# Unpacking the tuple
name, age, occupation = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Occupation: {occupation}")


# Program to combine two tuples
fruits = ("apple", "banana")
more_fruits = ("cherry", "date")
combined_fruits = fruits + more_fruits
print("Combined tuple:", combined_fruits)


# Program to find an element in a tuple
fruits = ("apple", "banana", "cherry", "date")
search_fruit = "banana"

if search_fruit in fruits:
  print(f"{search_fruit} is in the tuple.")
else:
  print(f"{search_fruit} is not in the tuple.")


# Program to count occurrences & find the index of an element in a tuple
fruits = ("apple", "banana", "cherry", "banana", "date")
count = fruits.count("banana")
index = fruits.index("banana")

print(f"Number of occurrences of 'banana': {count}")
print(f"Index of the 'cherry': {index}")