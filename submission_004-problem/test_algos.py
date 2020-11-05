import unittest
import super_algos
from super_algos import *

class TestSuper_algos(unittest.TestCase):
    '''
    This tests that the function returns -1 if the list is empty or if there's an invalid character in the list.
    It tests that it returns the lowest value in a list whether there are negative or positive numbers in it.
    It tests to return the first index if only one number is given
    '''
    
    def test_find_min(self):
        
        self.assertEqual(-1, super_algos.find_min([]))
    
        self.assertEqual(-1, super_algos.find_min(["a"]))
    
        self.assertEqual(2, super_algos.find_min([3,12,9,2,11]))
    
        self.assertEqual(7, super_algos.find_min([7]))
    
        self.assertEqual(-5, super_algos.find_min([-1,-2,-3,-4,-5]))


    def test_sum_all(self):
    
        '''
        This tests that the function returns -1 if the list is empty or if there's an invalid character in the list.
        It tests that it returns the sum of all numbers in a list whether they are negative or positive numbers.
        It tests to return the first index if only one number is given
        '''
    
        self.assertEqual(-1, super_algos.sum_all([]))
    
        self.assertEqual(-1, super_algos.sum_all(["a"]))
    
        self.assertEqual(7, super_algos.sum_all([7]))
    
        self.assertEqual(60, super_algos.sum_all([10,20,30]))
    
        self.assertEqual(-60, super_algos.sum_all([-10,-20,-30]))


    def test_find_possible_strings(self):
    
        '''
        This tests that the function returns an empty list if empty or if there's an invalid character in the list.
        It also tests that it prints all permutations of a given list of strings and that its the correct length.
        '''
    
        self.assertEqual([], super_algos.find_possible_strings([], 3))
    
        self.assertEqual([], super_algos.find_possible_strings([1], 3))
    
        self.assertEqual(["a","b"], super_algos.find_possible_strings(["a","b"], 1))
    
        self.assertEqual(["aaa", "aab", "aba", "abb", "baa", "bab", "bba", "bbb"],
        super_algos.find_possible_strings(["a","b"], 3))

if __name__ == '__main__':
    unittest.main()