# Open a file for writing
with open("example.txt", "w") as file:
    # Write data to the file
    file.write("Hello, world!\n")
    file.write("This is a test file.\n")

# Open the file for reading
with open("example.txt", "r") as file:
    # Read the entire file
    content = file.read()
    print("File content:")
    print(content)

# Append data to the file
with open("example.txt", "a") as file:
    file.write("This is a new line.\n")

# Read from the file line by line
with open("example.txt", "r") as file:
    print("File content line by line:")
    for line in file:
        print(line.strip())

# Check if a file exists
import os.path

if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File does not exist.")
