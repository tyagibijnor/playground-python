# Example 1: Simple function
def greet(name):
    return f"Hello, {name}!"

# Example 2: Function with default argument
def add(a, b=5):
    return a + b

# Example 3: Function with variable arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Example 4: Function returning multiple values
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Example 5: Lambda function
square = lambda x: x * x

# Example 6: Function with keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



# Example usage
if __name__ == "__main__":
    print(greet("Navneet"))
    print(add(10))
    print(multiply(2, 3, 4))
    q, r = divide_and_remainder(10, 3)
    print(f"Quotient: {q}, Remainder: {r}")
    print(square(7))
    print_info(name="Bob", age=25)
    print("All tests passed!")
    
## method 1: Using assert statements
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)  # Should return 120
assert factorial(5) == 120, "Test failed: factorial(5) should return 120"
assert factorial(0) == 1, "Test failed: factorial(0) should return 1"
assert factorial(1) == 1, "Test failed: factorial(1) should return 1"
print("All factorial tests passed!")

## method 2: Using unittest framework
import unittest 
class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)   
    
## method 3: with input and output
def test_factorial():   
    test_cases = [
        (5, 120),
        (0, 1),
        (1, 1),
        (3, 6),
        (4, 24)
    ]
    
    for n, expected in test_cases:
        result = factorial(n)
        assert result == expected, f"Test failed: factorial({n}) should return {expected}, got {result}"
    
    print("All factorial tests passed!")
    
val1 =int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {val1} is {factorial(val1)}")  