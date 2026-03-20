## Pallindrom test
def is_palindrome(s):   
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
# Test cases
assert is_palindrome("A man, a plan, a canal, Panama") == True, "Test failed: Should be a palindrome"
assert is_palindrome("racecar") == True, "Test failed: Should be a palindrome   "
assert is_palindrome("hello") == False, "Test failed: Should not be a palindrome    "
assert is_palindrome("Was it a car or a cat I saw?") == True,   "Test failed: Should be a palindrome"
assert is_palindrome("No 'x' in Nixon") == True, "Test failed:      Should be a palindrome"
assert is_palindrome("Not a palindrome") == False, "Test failed: Should not be a palindrome"
print("All palindrome tests passed!")   