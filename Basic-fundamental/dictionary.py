## Dictonary of words and their definitions
dictionary = {
    "python": "a high-level programming language",  
    "algorithm": "a step-by-step procedure for solving a problem",
    "data": "facts and statistics collected together for reference or analysis",
    "function": "a block of organized, reusable code that performs a single action",
    "variable": "a storage location paired with an associated symbolic name",
    "loop": "a programming construct that repeats a block of code while a condition is true"
}
print("Dictionary of words and their definitions:", dictionary)

## disctionary methods
print("Keys in the dictionary:", dictionary.keys()) # This will return a view object that displays a list of all the keys in the dictionary
print("Values in the dictionary:", dictionary.values()) # This will return a view object that displays a list of all the values in the dictionary
print("Items in the dictionary:", dictionary.items()) # This will return a view object that displays a list of all the key-value pairs in the dictionary as tuples
print("Definition of 'python':", dictionary.get("python")) # This will return the value associated with the key "python" in the dictionary
print("Definition of 'algorithm':", dictionary.get("algorithm")) # This will return the value associated with the key "algorithm" in the dictionary
print("Definition of 'data':", dictionary.get("data")) # This will return the value associated with the key "data" in the dictionary
print("Definition of 'function':", dictionary.get("function")) # This will return the value associated with the key "function" in the dictionary
print("Definition of 'variable':", dictionary.get("variable")) # This will return the value associated with the key "variable" in the dictionary
print("Definition of 'loop':", dictionary.get("loop")) # This will return the value associated with the key "loop" in the dictionary

## dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)} # This will create a new dictionary that contains the numbers from 1 to 5 as keys and their squares as values using dictionary comprehension
print("Dictionary of numbers and their squares:", squared_dict)

## disctionary with nested structures
nested_dict = { 
    "level1": {
        "level2": {
            "key1": "value"
        }
    }
}
print("Nested dictionary:", nested_dict)

## dictionary with mixed data types
mixed_dict = {
    "string_key": "string_value",
    42: "integer_key",
    3.14: "float_key",
    True: "boolean_key"
}
print("Dictionary with mixed data types:", mixed_dict) 

## dictionary with list as values
list_dict = {
    "fruits": ["apple", "banana", "orange"],
    "colors": ["red", "green", "blue"]
}
print("Dictionary with list as values:", list_dict) 

## dictionary with tuple as keys
tuple_dict = {
    (1, 2): "value1",
    (3, 4): "value2"
}
print("Dictionary with tuple as keys:", tuple_dict)

## accessing nested dictionary values
nested_value = nested_dict["level1"]["level2"]["key1"] # This will access the value associated with the key "key1" in the nested dictionary
print("Accessed value from nested dictionary:", nested_value)

## methods for dictionary 
dictionary["new_key"] = "new_value" # This will add a new key-value pair to the dictionary
print("Dictionary after adding new key-value pair:", dictionary)    