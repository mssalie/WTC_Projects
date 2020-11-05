from io import StringIO
import unittest
from unittest.mock import patch
import mastermind
import io
import sys
from mastermind import *

class TestMastermind(unittest.TestCase):

    def test_create_code(self):
        
        '''
        This tests if "create_code()" returns a value with 4 digits,
        where each digit is in the range 1 to 8.This test also calls "create_code()" 100 times.
        '''
        
        for i in range(100):
            
            self.assertNotIn(0, mastermind.create_code())
            self.assertNotIn(9, mastermind.create_code())
            self.assertEqual(len(mastermind.create_code()), 4)


    def test_check_correctness(self):
        
        '''
        This tests the function "check_correctness()" where the function returns True or False.
        It tests that the function outputs "Congratulations! You are a codebreaker!" if True.
        If False, it outputs the correct amount of turns.
        '''
        
        sys.stdout = io.StringIO()
        self.assertTrue(mastermind.check_correctness(6, 4))
        self.assertEqual(sys.stdout.getvalue(), 'Congratulations! You are a codebreaker!\n')
        
        sys.stdout = io.StringIO()
        self.assertFalse(mastermind.check_correctness(6, 3))
        self.assertEqual(sys.stdout.getvalue(), 'Turns left: 6\n')


    @patch("sys.stdin", StringIO("123\n12345\n1234\n"))
    def test_get_answer_input(self):
        
        '''
        This function tests if "get_answer_input()" returns the users input if the condition is met(4 digit code).
        If it is less than or more than 4 digit code it'll prompt the user for input again.
        '''
        
        sys.stdout = io.StringIO()
        self.assertEqual(mastermind.get_answer_input(),"1234")
        self.assertEqual(sys.stdout.getvalue(), '''Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ''')


    def test_take_turn(self):
        
        '''This test checks that "correct_digits_and_position" and "correct_digits_only" updates correctly'''
        
        self.assertEqual(mastermind.take_turn([3,8,5,9], [3,5,8,9]), (2,2))
        self.assertEqual(mastermind.take_turn([5,4,3,2], [1,2,3,4]), (1,2))
        self.assertEqual(mastermind.take_turn([1,2,3,4], [1,2,3,4]), (4,0))

if __name__ == '__main__':
    unittest.main()