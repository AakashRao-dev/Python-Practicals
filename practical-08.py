# PRACTICAL-8 - PROGRAMS ON STRINGS

# Program to concatenate two strings
str1 = 'Hello, '
str2 = 'Aakash'

concatenated_string = str1 + str2
print(concatenated_string)

# -------------------------------------------

# Program to find the length of a string
str3 = 'JavaScript is an amazing language, better than Python'

length = len(str3)
print(f'The length of the string is {str3} characters')

# -------------------------------------------

# Program to slice a string
str4 = 'Python is weird. JavaScript is cool.'

# slicing the string
sub_string = str4[16:]
print(f'Substring:{sub_string}')

# -------------------------------------------

# Program to use string methods
str5 = 'JavaScript can be used for Backend Programming!'

# Converting to Uppercase
uppercase_string = str5.upper()
print(f'Uppercase string: {uppercase_string}')


# Converting to Lowercase
lowercase_string = str5.lower()
print(f'Lowercase string: {lowercase_string}')

# Replace a substring
replaced_string = str5.replace('JavaScript', 'Python')
print(f'Replaced string: {replaced_string}')

# -------------------------------------------

# Program to split a string into a list
str6 = 'Python is a versatile language, it can be used for a wide range of applications'

# Split the string by commas
split_list = str6.split(',')
print(split_list)