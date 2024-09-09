# PRACTICAL-3:

# Program to create a list and access its elements
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements of a list
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Slicing the list:", fruits[1:3])

# Program to modify a list
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # adding an element to the end
numbers[2] = 10 # modifying an element
numbers.remove(4) # removing an element
print(numbers)

# Program to iterate over a list
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# Program to create a new list using list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# Program to find an element in a list
fruits = ["apple", "banana", "cherry", "date"]
search_fruit = "banana"

if search_fruit in fruits:
  print(f"{search_fruit} is in the list")
else:
  print(f"{search_fruit} is not in the list")

# Program to sort & reverse a list
numbers = [3, 1, 4, 2, 5]
numbers.sort() # sorting the list in ascending order
print("Sorted list: ", numbers)

numbers.reverse() # reversing the list
print("Reversed list: ", numbers)