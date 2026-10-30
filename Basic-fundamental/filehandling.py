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

## Reading words and counting them
with open('example.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print(f"Total words in the file: {word_count}")
    print(f"Words: {words}")

## file handling with dictionaries
# Writing a dictionary to a file
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('person.txt', 'w') as file:
    for key, value in person.items():
        file.write(f"{key}: {value}\n")
# Reading a dictionary from a file
with open('person.txt', 'r') as file:
    person_dict = {}
    for line in file:
        key, value = line.strip().split(': ')
        person_dict[key] = value
    print(f"Person from file: {person_dict}")

## reading a file line by line and count characters in each line
with open('example.txt', 'r') as file:
    for line in file:
        char_count = len(line)
        print(f"Line: {line.strip()} - Characters: {char_count}")