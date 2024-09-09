# PRACTICAL-1:

# IF-ELSE
# Program to determine if a given number is even or odd
num = int(input("Enter a number: "))
if (num % 2 == 0):
  print(f"{num} number is Even.")
else:
  print(f"{num} number is Odd.")


# WHILE LOOP
# Program to print numbers from 1 to 5 using while loop
count = 1
while count <= 5:
  print(count)
  count += 1


# FOR LOOP
# Program to calculate the sum of numbers from 1 to 10 using a for loop
sum = 0
for i in range(1, 11):
  sum += i
print("Sum of numbers from 1 to 10 is :", sum)

# NESTED LOOP
# Program to print a pattern of stars using nested loops
n = 5
for i in range(1, n + 1):
  for j in range(i):
    print("*",end="")
  print()


# BREAK & CONTINUE
# Program to find the first even numbers in a list & continue to find the next number if odd

numbers = [7, 12, 5, 8, 3, 10]
for num in numbers:
  if num % 2 == 0:
    print(f"The first even number in the list is {num}")
    break
  else:
    continue


# SWITCH CASE
# Program that performs basic arithmetic operations (addition, subtraction, multiplication, division) using a dictionary with dictionary.

# Define arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handle division by zero
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Dictionary to simulate switch-case
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

# Take user input for the operation and numbers
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get the function from the dictionary and execute it
result = operations.get(operation, lambda x, y: "Invalid operation")(num1, num2)

# Print the result
print(f"Result: {result}")