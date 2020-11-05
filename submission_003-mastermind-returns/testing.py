import unittest
from unittest.mock import patch
from io import StringIO

def get_answer_input():
    return input('Enter your guess: ') 

class TestFunctions(unittest.TestCase):

    @patch("sys.stdin", StringIO("answer\nanswer2\n"))
    def test_compare(self):
        self.assertEqual(get_answer_input(), "answer")
        self.assertEqual(get_answer_input(), "answer2")

if __name__ == '__main__':
    unittest.main()