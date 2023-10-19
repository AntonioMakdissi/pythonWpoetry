"""
This script contains unit tests for the 'first_word' function from the 'funct' module.
"""
import unittest
from python_w_poetry import funct

class TestFirstWordFunction(unittest.TestCase):
    """ A test suite for the 'first_word' function.

    This test suite includes multiple test cases to verify the behavior of the 'first_word' function
    when extracting the first word from different types of input texts.
    """
    def test_single_word(self):
        """
        Test case to extract the first word from a text containing a single word.
        """
        text = "Hello, World!"
        self.assertEqual(funct.first_word(text), "Hello")

    def test_empty_string(self):
        """
        Test case to extract the first word from an empty string.
        """
        text = ""
        self.assertEqual(funct.first_word(text), "")

    def test_special_characters(self):
        """
        Test case to extract the first word from a text containing special characters.
        """
        text = "$$$Money talks!!!"
        self.assertEqual(funct.first_word(text), "Money")

    def test_apostrophe(self):
        """
        Test case to extract the first word from a text containing an apostrophe.
        """
        text = "I'm learning Python."
        self.assertEqual(funct.first_word(text), "I'm")

    def test_spacestart(self):
        """
        Test case to extract the first word when the text starts with a space.
        """
        assert funct.first_word(" a word ") == "a"

    def test_points(self):
        """
        Test case to extract the first word from a text containing ellipsis points.
        """
        assert funct.first_word("... and so on ...") == "and"

if __name__ == '__main__':
    unittest.main() #
