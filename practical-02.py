# PRACTICAL-2:

# ARITHMETIC OPERATIONS
# Program to perform arithmetic operations on two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")


# COMPARISON OPERATORS
# Program to compare two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")


# LOGICAL OPERATORS
# Program to check if a number is within a given range

num = int(input("Enter a number: "))
lower_limit = 30
upper_limit = 90

if num >= lower_limit and num <= upper_limit:
    print(f"{num} is within the range of {lower_limit} and {upper_limit}.")
else:
  print(f"{num} is outside the range.")

# INPUT/OUTPUT OPERATIONS
# Program to read and write a text file

# Writing to a text file
with open("aakash.txt", "w") as file:
    file.write("Hello, this is Aakash.\n")
    file.write("I'm a Fullstack Developer, I love to build complex logic for backend for beautiful UIs.\n")
    file.write("I hate Python as a programming language")

# Reading from the same text file
with open("aakash.txt", "r") as file:
  content = file.read()
  print("File content:\n")
  print(content)


# STRING OPERATIONS
# Program to concatenate two strings
str1 = "Hello, this is"
str2 = " Aakash"
concatenated_str = str1 + str2
print(concatenated_str)

# Program to repeat a string
original_str = "LinkedIn, "
repeated_str = original_str * 3
print(repeated_str)