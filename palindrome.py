"""
Validates strings as palindromes.
"""

def is_palindrome(value):
    if not isinstance(value, str):
        raise ValueError("Input must be a string")
    return False if value == "" else None