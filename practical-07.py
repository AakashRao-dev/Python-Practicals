# PRACTICAL-7 - PROGRAMS ON FILE HANDLING

# Program to write data to a text file
file_name = "aakash_codes.txt"

# Opening the file in write mode
with open(file_name, "w") as file:
  file.write("I'm Aakash, a FullStack Web Developer & UI Designer.\n")
  file.write("I love to design & bring those design to live with code on the web")

print(f"Data written to '{file_name}' successfully!")


# ----------------------------------------

# Program to read data from a text file
file_name = "aakash_codes.txt"

# Opening the file in read mode
with open(file_name, "r") as file:
  content = file.read()

print("File Contents:\n" + content)

# ----------------------------------------

# Program to append data to an exisiting text file
file_name = "aakash_codes.txt"

# Opening the file in append mode
with open(file_name, "a") as file:
  file.write("\nThis is an additional line added to the file.")

print("Data appended to the file successfully. Enjoy!")

