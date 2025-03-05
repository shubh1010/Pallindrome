"""
Tests the palindrome module
"""

import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_raises_value_error_for_non_string(self):
        with self.assertRaises(ValueError):
            is_palindrome(123)

    def test_empty_string_returns_false(self):
        self.assertFalse(is_palindrome(""))

    def test_single_character_is_palindrome(self):
        self.assertTrue(is_palindrome("a"))

    def test_two_identical_characters_are_palindrome(self):
        self.assertTrue(is_palindrome("bb"))

if __name__ == "__main__":
    unittest.main()