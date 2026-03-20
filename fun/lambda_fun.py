# Lambda Function Examples in Python

# Example 1: Simple lambda for addition
add = lambda x, y: x + y
print(f"Add 5 + 3: {add(5, 3)}")

# Example 2: Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

# Example 3: Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Example 4: Lambda with sorted()
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Students sorted by grade: {sorted_students}")

# Example 5: Lambda with sorting strings
words = ['python', 'code', 'lambda', 'function']
sorted_words = sorted(words, key=lambda x: len(x))
print(f"Words sorted by length: {sorted_words}")

# Example 6: Lambda with reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers: {product}")
