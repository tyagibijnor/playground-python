## Password test
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        return False
    return True 
# Test cases
assert is_valid_password("Password123!") == True, "Test failed: Valid password should return True"
assert is_valid_password("short") == False, "Test failed: Password too short should return False"
assert is_valid_password("nouppercase1!") == False, "Test failed: Password without  uppercase should return False"
assert is_valid_password("NOLOWERCASE1!") == False, "Test failed: Password without lowercase should return False"
assert is_valid_password("NoDigits!") == False, "Test failed: Password without digits should return False"  
assert is_valid_password("NoSpecialChar1") == False, "Test failed: Password without special characters should return False"
print("All password tests passed!") 
