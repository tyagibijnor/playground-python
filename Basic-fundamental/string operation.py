"""Examples of common Python string operations."""

name = "My name is Navneet Tyagi"
print(f"Indexing [0] (gets the first character): {name[0]}")
print(f"Indexing [-1] (gets the last character): {name[-1]}\n")

# Repeat a string with the * operator.
print("String repetition (repeats the string 5 times):")
print(f"{name}\n" * 5)

print(f"'in' (checks whether 'Tyagi' is present): {'Tyagi' in name}")
print(f"'in' (checks whether 'kumar' is present): {'kumar' in name}")

# Count occurrences of a substring with str.count().
sentence = "I am learning generative ai, as ai is required for now"
print(f"count('ai') (counts occurrences in sentence): {sentence.count('ai')}")

text = "Hello, World!"
print(f"len(text) (returns the number of characters): {len(text)}")
print(f"count('l') (counts occurrences in text): {text.count('l')}")

word = "banana"
print(f"count('an') (counts substring occurrences in word): {word.count('an')}")

# Capitalize the first character and lowercase the rest.
message = "hello, and welcome to my world."
print(f"capitalize() (capitalizes the first character): {message.capitalize()}")

# Use common string methods.
text = "  Python string methods are useful!  "
print(f"lower() (converts all letters to lowercase): {text.lower()}")
print(f"upper() (converts all letters to uppercase): {text.upper()}")
print(f"title() (capitalizes the first letter of each word): {text.title()}")
print(f"strip() (removes whitespace from both ends): {text.strip()}")
print(
    "replace('useful', 'powerful') (replaces matching text): "
    f"{text.replace('useful', 'powerful')}"
)

# Split and join strings.
fruits = "apple,banana,mango"
fruit_list = fruits.split(",")
print(f"split(',') (splits a string into a list): {fruit_list}")
print(f"join() (joins list items with ' - '): {' - '.join(fruit_list)}")

# Search strings.
print(
    f"find('string') (returns its starting index, or -1 if absent): "
    f"{text.find('string')}"
)
print(
    f"startswith('  Python') (checks the beginning of the string): "
    f"{text.startswith('  Python')}"
)
print(
    f"endswith('!  ') (checks the end of the string): "
    f"{text.endswith('!  ')}"
)

# Check string contents.
print(f"isalpha() (checks whether all characters are letters): {'Python'.isalpha()}")
print(f"isalnum() (checks for letters or digits only): {'Python3'.isalnum()}")
print(f"isdigit() (checks whether all characters are digits): {'2026'.isdigit()}")
print(f"isspace() (checks whether all characters are whitespace): {'   '.isspace()}")
