## File Handling
# Open a file for reading
file = open('example.txt', 'r')
# Read the contents of the file
content = file.read()
print(content)
# Close the file
file.close()
## Open a file for writing
file = open('example.txt', 'w')
# Write some content to the file
file.write("Hello, this is an example file.\n")
file.write("This file is used for demonstrating file handling in Python.\n")
# Close the file
file.close()
## Open a file for appending
file = open('example.txt', 'a')
# Append some content to the file
file.write("This is an additional line appended to the file.\n")
# Close the file
file.close()
## Open a file for reading and writing
file = open('example.txt', 'r+')
# Read the current contents of the file
content = file.read()
print(content)
# Move the cursor to the beginning of the file  
file.seek(0)
# Write new content to the file (this will overwrite the existing content) 
file.write("This content will overwrite the existing content.\n")
# Close the file
file.close()
## with statement for file handling (automatically closes the file)
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

## File handling with lists
# Writing a list to a file
fruits = ['apple', 'banana', 'cherry', 'date']
with open('fruits.txt', 'w') as file:
    for fruit in fruits:
        file.write(fruit + '\n')
# Reading a list from a file
with open('fruits.txt', 'r') as file:
    fruit_list = file.readlines()
    # Remove newline characters from each fruit
    fruit_list = [fruit.strip() for fruit in fruit_list]
    print(f"Fruits from file: {fruit_list}")    
