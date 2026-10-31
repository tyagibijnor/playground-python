"""A practical guide to Python lists and their most-used methods.

Run this file to see the examples. Lists are ordered, mutable collections;
they can contain values of different types and may contain duplicates.
"""


# Creating lists
empty = []
numbers = [10, 20, 30, 20]
mixed = ["apple", 3, True]
from_range = list(range(1, 5))  # [1, 2, 3, 4]
print("Created:", empty, numbers, mixed, from_range)

# Reading values: indexes start at 0; negative indexes count from the end.
print("First and last:", numbers[0], numbers[-1])
print("Slice [1:3]:", numbers[1:3])  # start included, end excluded
print("Length and membership:", len(numbers), 20 in numbers)

# append(value): add one item to the end; changes the original list.
items = ["pen", "book"]
items.append("cup")
print("append:", items)

# extend(iterable): add each item from an iterable to the end.
items.extend(["key", "map"])
print("extend:", items)

# insert(index, value): add an item at a position; later items shift right.
items.insert(1, "pencil")
print("insert:", items)

# remove(value): remove the first matching value; raises ValueError if absent.
items.remove("cup")
print("remove:", items)

# pop([index]): remove and return an item (last item by default).
last_item = items.pop()
second_item = items.pop(1)
print("pop results and remaining list:", last_item, second_item, items)

# index(value[, start[, end]]): position of the first match; raises ValueError
# if absent. count(value): number of matching items.
print("index and count:", numbers.index(20), numbers.count(20))

# sort(*, key=None, reverse=False): sort in place; returns None.
scores = [42, 7, 19, 7]
scores.sort()
print("sort ascending:", scores)
scores.sort(reverse=True)
print("sort descending:", scores)
words = ["pear", "fig", "watermelon"]
words.sort(key=len)  # sort by word length
print("sort with key:", words)

# sorted(iterable) returns a new sorted list, leaving the original unchanged.
original = [3, 1, 2]
ordered = sorted(original)
print("sorted copy:", ordered, "original:", original)

# reverse(): reverse the list in place; it does not sort the values.
letters = ["a", "b", "c"]
letters.reverse()
print("reverse:", letters)

# copy(): make a shallow copy. A nested list inside is still shared.
source = [1, 2, 3]
copied = source.copy()  # source[:] and list(source) also make shallow copies
copied.append(4)
print("copy:", "source =", source, "copied =", copied)

# clear(): remove every item from the list in place.
temporary = [1, 2]
temporary.clear()
print("clear:", temporary)

# Lists also support concatenation (+), repetition (*), and item assignment.
combined = [1, 2] + [3, 4]
repeated = ["ha"] * 3
combined[0] = 99
print("operators and assignment:", combined, repeated)

# A comprehension is a concise way to build a new list.
squares = [number**2 for number in range(5)]
even_squares = [number**2 for number in range(6) if number % 2 == 0]
print("comprehensions:", squares, even_squares)

# Mutating methods such as append, extend, insert, sort, reverse, and clear
# change the list directly and return None. Do not assign their result back
# (for example, `items = items.sort()` is a mistake).


# Tuples: ordered collections that cannot be structurally changed after creation.
empty_tuple = ()
coordinates = (4, 7)
mixed_tuple = ("apple", 3, True)
from_range_tuple = tuple(range(1, 5))
print("Tuples:", empty_tuple, coordinates, mixed_tuple, from_range_tuple)

# Parentheses are optional in many contexts; the comma makes a tuple.
single_item_tuple = ("only item",)
also_a_tuple = "only item",
not_a_tuple = ("only item")  # parentheses alone do not create a tuple
print("Single-item tuple:", single_item_tuple, also_a_tuple, type(not_a_tuple))

# Tuples support indexing, negative indexing, slicing, length, and membership.
print("Tuple access:", coordinates[0], coordinates[-1], coordinates[0:1])
print("Tuple length and membership:", len(mixed_tuple), "apple" in mixed_tuple)

# Tuples have two commonly used methods: count and index.
repeated_values = (1, 2, 1, 3, 1)
print("Tuple count and index:", repeated_values.count(1), repeated_values.index(3))

# Unpacking assigns tuple values to variables; * collects remaining values.
x, y = coordinates
first, *middle, last = (10, 20, 30, 40)
print("Unpacking:", x, y, first, middle, last)

# A tuple cannot be changed in place; make a new tuple to add or remove values.
more_coordinates = coordinates + (9,)
repeated_coordinates = coordinates * 2
print("Tuple concatenation and repetition:", more_coordinates, repeated_coordinates)
# coordinates[0] = 5  # TypeError: tuple items cannot be assigned

# A tuple can contain a mutable object. The tuple reference is fixed, but the
# contained list can still change.
tuple_with_list = ("colors", ["red", "blue"])
tuple_with_list[1].append("green")
print("Mutable item inside tuple:", tuple_with_list)

# List vs tuple: both are ordered, allow duplicates, indexing, and iteration.
# Lists are mutable and have many in-place methods; tuples are immutable and
# generally suit fixed records or values that should not be reassigned.
list_version = ["latitude", 40.7, "longitude", -74.0]
tuple_version = ("latitude", 40.7, "longitude", -74.0)
list_version[1] = 41.0
# tuple_version[1] = 41.0  # TypeError: tuple items cannot be assigned
print("List vs tuple after item update:", list_version, tuple_version)

# Lists provide methods such as append, extend, remove, sort, and clear.
# Tuples do not have these methods; convert to a list to edit, then back.
editable = list(tuple_version)
editable.append("updated")
updated_tuple = tuple(editable)
print("Convert, edit, convert back:", updated_tuple)

# Tuples can be dictionary keys when all their items are hashable; lists cannot.
locations = {(40.7, -74.0): "New York"}
print("Tuple as dictionary key:", locations[(40.7, -74.0)])
# {[40.7, -74.0]: "New York"}  # TypeError: lists are unhashable


