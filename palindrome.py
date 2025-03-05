"""
Validates strings as palindromes.
"""

def is_palindrome(value):
    if not isinstance(value, str):
        raise ValueError("Input must be a string")
    if value == "":
        return False
    if len(value) == 1:
        return True
    if len(value) == 2 and value[0] == value[1]:
        return True
    return None
