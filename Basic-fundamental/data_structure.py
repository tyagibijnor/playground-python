## Datastructure in python
# List
my_list = [1, 2, 3, 4, 5]
# Tuple
my_tuple = (1, 2, 3, 4, 5,5)
# Set
my_set = {1, 2, 3, 4, 5, 5}
# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# String
my_string = "Hello, World!"

print ("List:", my_list)
print ("Tuple:", my_tuple)
print ("Set:", my_set)
print ("Dictionary:", my_dict)
print ("String:", my_string)
print("Split List:",my_list[0:2])
print("Split List:",my_list[:3])
print("Split List:",my_list[-2])
print("Main List:",my_list)
my_list[2]=15
print("Updated List:",my_list)
## List are mutable, we can change the value of list but tuple are immutable we can't change the value of tuple
# my_tuple[2]=15 # This will raise an error because tuple is immutable 
## Set is also mutable but it does not allow duplicate values, so it will only keep one instance of the value 5 in the set.
# my_set[2]=15 # This will raise an error because set is mutable but it does not support indexing
my_dict['c']=15 # This will update the value of key 'c' to 15 in the dictionary
print("Updated Dictionary:",my_dict)
## String is immutable, we can't change the value of string
# my_string[0]='h' # This will raise an error because string is immutable
# We can use slicing to get a substring from the string
substring = my_string[0:5] # This will get the substring "Hello" from the string
print("Substring:", substring) 
## We can also use string concatenation to create a new string
new_string = my_string + " How are you?" # This will create a new string "Hello, World! How are you?" by concatenating the original string with another string
print("New String:", new_string)
# We can also use string formatting to create a new string
formatted_string = "My name is {} and I am {} years old.".format("Tyagi", 30) # This will create a new string "My name is Tyagi and I am 30 years old." by using string formatting
print("Formatted String:", formatted_string)
## We can also use f-strings to create a new string
name = "Tyagi"
age = 30
f_string = f"My name is {name} and I am {age} years old." # This will create a new string "My name is Tyagi and I am 30 years old." by using f-strings
print("F-String:", f_string)
# Loops
# For loop to iterate over a list
for i in my_list:
    print(i)
print(" LIST ",my_list[0:3])
players = ["Alice", "Bob", "Charlie", "David", "Eve"]
# For loop to iterate over a list of players    
for player in players:
    print(player)

print("Players List:", players[0:3])
print("Players List:", players[:3])
print("Players List:", players[-4:])
print("Players List:", players[:-3])
