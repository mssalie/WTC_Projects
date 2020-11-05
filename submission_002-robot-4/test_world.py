import unittest
from world.text import world
from unittest.mock import patch
from io import StringIO
import sys

class TestWorld(unittest.TestCase):

    def test_is_position_allowed(self):
        
        self.assertEqual(world.is_position_allowed(101,201), False)
        self.assertEqual(world.is_position_allowed(10,201),False)
        self.assertEqual(world.is_position_allowed(101,10), False)
        self.assertEqual(world.is_position_allowed(10,10), True)


if __name__ == '__main__':
    unittest.main()