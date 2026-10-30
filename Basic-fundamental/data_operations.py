##list operations 
my_list = [3, 11, 1, 2, 3, 50, 5]
## append
print("List :", my_list)
my_list.append(4) # This will add the value 4 to the end of the list
print("List after append:", my_list)

## insert
my_list.insert(1, 10) # This will insert the value 10 at index 1 in the list
print("List after insert:", my_list)

## remove
my_list.remove(2) # This will remove the first occurrence of the value 2 from the list
print("List after remove:", my_list)

## index
index_of_3 = my_list.index(3) # This will return the index of the first occurrence of the value 3 in the list
print("Index of 3:", index_of_3)

## count
count_of_3 = my_list.count(3) # This will return the number of occurrences of the value 3 in the list
print("Count of 3:", count_of_3)

## size
size_of_list = len(my_list) # This will return the number of elements in the list
print("Size of list:", size_of_list) 

# sort
my_list.sort() # This will sort the list in ascending order
print("List after sort:", my_list)

## reverse
my_list.reverse() # This will reverse the order of the elements in the list
print("List after reverse:", my_list)

## pop
popped_value = my_list.pop() # This will remove and return the last element of the  list
print("Popped value:", popped_value)

popped_value_at_index_2 = my_list.pop(2) # This will remove and return the element at index 2 in the list
print("Popped value at index 2:", popped_value_at_index_2) 
print("List after pop:", my_list)

## clear
my_list.clear() # This will remove all the elements from the list
print("List after clear:", my_list) 

## insert
my_list.insert(0, 1) # This will insert the value 1 at index 0 in the list
my_list.insert(1, 2) # This will insert the value 2 at index 1 in the list
my_list.insert(2, 3) # This will insert the value 3 at index 2 in the list
my_list.insert(3, 4) # This will insert the value 4 at index    3 in the list
my_list.insert(4, 5) # This will insert the value 5 at index 4 in the list
print("List after inserting values:", my_list)

## enumerate
for index, value in enumerate(my_list): # This will iterate over the list and return both the index and the value of each element in the list
    print("Index:", index, "Value:", value)

## len
length_of_list = len(my_list) # This will return the number of elements in the list
print("Length of list:", length_of_list)

## comprehension
squared_list = [x**2 for x in my_list] # This will create a new list that contains the squares of the elements in the original list using list comprehension
print("Squared list:", squared_list)

## range
for i in range(5): # This will iterate over the range of numbers from 0 to 4 and print each number
    print("Range value:", i)
    
## loop with range
for i in range(len(my_list)): # This will iterate over the range of numbers from 0 to the length of the list and print the index and the value of each element in the list
    print("Index:", i, "Value:", my_list[i])

for i in range(60, 70): # This will iterate over the range of numbers from 1 to 5 and print each number
    my_list.append(i)
print("List after appending range values:", my_list)

## nested loop
for i in range(3): # This will iterate over the range of numbers from 0 to 2 and print the value of i
    for j in range(3): # This will iterate over the range of numbers from 0 to 2 and print the value of j
        print("i:", i, "j:", j)

item_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
print("Original list of items:", item_list)
len_list = [len(item) for item in item_list] # This will create a new list that contains the lengths of the strings in the original list using list comprehension
print("List of item lengths:", len_list)

## nested list
pair =  [[i,j] for i in item_list for j in len_list]
print("Nested list of pairs:", pair)

## tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)   
print("Index of 3 in tuple:", my_tuple.index(3)) # This will return the index of the first occurrence of the value 3 in the tuple
print("Count of 3 in tuple:", my_tuple.count(3))  # This will return the number of occurrences of the value 3 in the tuple

a,b,c,d = (1,2,(2,3,4),'tyagi') # This will unpack the values from the tuple into the variables a, b, c, and d
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("Unpacked values from tuple:", a, b, c, d)
print("Unpacked values from tuple:", a, b, c[0], c[1], c[2], d)

name,*fruit,sweet = ('navneet','apple','mango','jalabi') # This will unpack the values from the tuple into the variable name and sweet, and the remaining values will be packed into the variable fruit using the * operator
print("Name:", name)
print("Fruit:", fruit)
print("Sweet:", sweet)

## loop for nested tuple
nested_tuple = ((1, 2), ("shiv", "ram"), (5, 6))
for inner_tuple in nested_tuple: # This will iterate over the outer tuple and print each inner tuple
    print("Inner tuple:", inner_tuple)
    for value in inner_tuple: # This will iterate over each inner tuple and print each value
        print("Value:", value)  
        
for i in nested_tuple: # This will iterate over the outer tuple and print each inner tuple
    ##print("Inner tuple:", i)
    for j in i: # This will iterate over each inner tuple and print each value
        print(j, sep=" ")
    print(" ")

tup_1=(1,2,3,4)
tup_2=(5,6,7,8)
tuple_3=tup_1+tup_2 # This will concatenate the two tuples and create a new tuple
print("Concatenated tuple:", tuple_3)
print("Extended tuple:", tuple_3*2) # This will repeat the elements of the tuple twice and create a new tuple