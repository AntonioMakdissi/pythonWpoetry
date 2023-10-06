from python_w_poetry import funct
import unittest

class TestFirstWordFunction(unittest.TestCase):

    def test_single_word(self):
        text = "Hello, World!"
        self.assertEqual(funct.first_word(text), "Hello")

    def test_empty_string(self):
        text = ""
        self.assertEqual(funct.first_word(text), "")

    def test_special_characters(self):
        text = "$$$Money talks!!!"
        self.assertEqual(funct.first_word(text), "Money")

    def test_apostrophe(self):
        text = "I'm learning Python."
        self.assertEqual(funct.first_word(text), "I'm")

    def test_spacestart(self):
        assert funct.first_word(" a word ") == "a"
    
    def test_points(self):
        assert funct.first_word("... and so on ...") == "and"

if __name__ == '__main__':
    unittest.main()





