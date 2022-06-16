"""This module allows to unitest our code in translator.py
if it passes we can go ahead, else we need to check the code"""
import unittest
from translator import english_to_french
from translator import french_to_english

class TestTranslator(unittest.TestCase):
    """It's class that inherits from unitest.TestCase base class
    in which we define all tests i.e functions that start with test_ prefixe"""
    def test_english_to_french1(self):
        """test passed/failed cases """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Null'), 'None')

    def test_french_to_english1(self):
        """test passed/failed cases """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Null'), 'None')


if __name__ == '__main__':
    unittest.main()
