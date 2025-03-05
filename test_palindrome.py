"""
Tests the palindrome module
"""

import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_function_exists(self):
        is_palindrome()

if __name__ == "__main__":
    unittest.main()