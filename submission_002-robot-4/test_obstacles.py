import unittest
from unittest.mock import patch
from io import StringIO
import sys
import world.obstacles as obs

class TestObstacles(unittest.TestCase):

    def test_is_position_blocked(self):

        obs.obstacles_list = [(10,10)]
        self.assertEqual(obs.is_position_blocked(10,10), True)
        self.assertEqual(obs.is_position_blocked(11,11), True)
        self.assertEqual(obs.is_position_blocked(20,20), False)


    def test_is_patch_blocked(self):
        
        obs.obstacles_list = [(10,10)]
        self.assertEqual(obs.is_path_blocked(0,10,10,10), True)
        self.assertEqual(obs.is_path_blocked(10,0,10,10), True)
        self.assertEqual(obs.is_path_blocked(0,0,10,0), False)
        self.assertEqual(obs.is_path_blocked(10,0,10,0), False)


if __name__ == '__main__':
    unittest.main()