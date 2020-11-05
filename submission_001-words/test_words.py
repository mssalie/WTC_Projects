import unittest
from word_processor import *
from io import StringIO
import sys

class TestWordProcessor(unittest.TestCase):

    def test_convert_to_word_list(self):
        
        '''
        This tests the function returns an empty list there if is no text given.
        It also checks it converts string to a list and removes all punctuation.
        '''

        self.assertEqual(convert_to_word_list(""), [])
        self.assertEqual(convert_to_word_list("These are indeed interesting, an obvious understatement, times. What say you?"),
['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement', 'times', 'what', 'say', 'you'])


    def test_words_longer_than(self):
        
        '''
        This tests the function returns an empty list if there is no text given.
        It tests that it returns all words in the string that are greater than the given length.
        '''

        self.assertEqual(words_longer_than(10, ""), [])
        self.assertEqual(words_longer_than(10, "These are indeed interesting, an obvious understatement, times. What say you?"),
['interesting', 'understatement'])


    def test_words_length_map(self):
        
        '''
        This tests the function returns an empty dictionary there is no text given.
        It tests the function returns a dictionary where the key is the length of the words.
        It test that the value is the ammount of time that word length occurs in the string.
        '''

        self.assertEqual(words_lengths_map(""), {})
        self.assertEqual(words_lengths_map("These are indeed interesting, an obvious understatement, times. What say you?"),
{2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1})


    def test_letters_count_map(self):
        
        '''
        This tests the function returns how many of each letter there is in a string.
        '''

        self.assertEqual(letters_count_map("These are indeed interesting, an obvious understatement, times. What say you?"),
{'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0,
'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3,
's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0})


    def test_most_used_character(self):

        '''
        This tests the function returns 'None' if no text is given.
        It tests that it returns the most used letter in a string.
        '''
        self.assertEqual(most_used_character(""), None)
        self.assertEqual(most_used_character("These are indeed interesting, an obvious understatement, times. What say you?"), "e")


if __name__ == '__main__':
    unittest.main()