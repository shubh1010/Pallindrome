"""
Tests the palindrome module
"""

import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindromes(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("Toronto"))
        self.assertFalse(is_palindrome("Hello, world!"))
        self.assertFalse(is_palindrome("Python"))
        self.assertFalse(is_palindrome("123abc321"))

if __name__ == "__main__":
    unittest.main()