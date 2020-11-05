import unittest
import robot
from robot import *
from unittest.mock import patch
from io import StringIO
import sys
import world.obstacles as obs


class TestRobot(unittest.TestCase):


    def test_store_history(self):
    
        self.assertEqual(robot.store_history("forward 10"), ["forward 10"])
        self.assertEqual(robot.store_history("right"), ["forward 10", "right"])


    def test_store_help_or_off(self):

        self.assertEqual(robot.store_history("help"), [])
        self.assertEqual(robot.store_history("off"), [])


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nreplay\noff\n"))
    def test_replay_command(self):
        
        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()
        

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,25).
 > jeff moved forward by 5 steps.
 > jeff now at position (0,30).
 > jeff replayed 2 commands.
 > jeff now at position (0,30).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nreplay silent\noff\n"))
    def test_silent_replay(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff replayed 2 commands silently.
 > jeff now at position (0,30).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nreplay reversed\noff\n"))
    def test_replay_reversed(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,20).
 > jeff moved forward by 10 steps.
 > jeff now at position (0,30).
 > jeff replayed 2 commands in reverse.
 > jeff now at position (0,30).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff replayed 2 commands in reverse silently.
 > jeff now at position (0,30).
jeff: What must I do next? jeff: Shutting down..
''')

    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nforward 3\nforward 1\nreplay 2\noff\n"))
    def test_replay_n(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,18).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,19).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,22).
 > jeff moved forward by 1 steps.
 > jeff now at position (0,23).
 > jeff replayed 2 commands.
 > jeff now at position (0,23).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nforward 3\nforward 1\nreplay 2 silent\noff\n"))
    def test_replay_silent_n(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,18).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,19).
jeff: What must I do next?  > jeff replayed 2 commands silently.
 > jeff now at position (0,23).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nforward 3\nforward 1\nreplay 2 reversed\noff\n"))
    def test_replay_reversed_n(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,18).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,19).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,24).
 > jeff moved forward by 10 steps.
 > jeff now at position (0,34).
 > jeff replayed 2 commands in reverse.
 > jeff now at position (0,34).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nforward 3\nforward 1\nreplay 2 reversed silent\noff\n"))
    def test_replay_silent_reversed_n(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,18).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,19).
jeff: What must I do next?  > jeff replayed 2 commands in reverse silently.
 > jeff now at position (0,34).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nforward 3\nforward 1\nreplay 4-2\noff\n"))
    def test_replay_n_to_m(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,18).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,19).
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,29).
 > jeff moved forward by 5 steps.
 > jeff now at position (0,34).
 > jeff replayed 2 commands.
 > jeff now at position (0,34).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nforward 3\nforward 1\nreplay 4-2 silent\noff\n"))
    def test_replay_silent_n_to_m(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,18).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,19).
jeff: What must I do next?  > jeff replayed 2 commands silently.
 > jeff now at position (0,34).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nforward 3\nforward 1\nreplay 4-2 reversed\noff\n"))
    def test_replay_reversed_n_to_m(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,18).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,19).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,20).
 > jeff moved forward by 3 steps.
 > jeff now at position (0,23).
 > jeff replayed 2 commands in reverse.
 > jeff now at position (0,23).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("jeff\nforward 10\nforward 5\nforward 3\nforward 1\nreplay 4-2 reversed silent\noff\n"))
    def test_replay_silent_reversed_n(self):

        obs.random.randint = lambda  a, b : 0
        sys.stdout = StringIO()
        robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? jeff: Hello kiddo!
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff now at position (0,15).
jeff: What must I do next?  > jeff moved forward by 3 steps.
 > jeff now at position (0,18).
jeff: What must I do next?  > jeff moved forward by 1 steps.
 > jeff now at position (0,19).
jeff: What must I do next?  > jeff replayed 2 commands in reverse silently.
 > jeff now at position (0,23).
jeff: What must I do next? jeff: Shutting down..
''')

if "__main__" == __name__:
    unittest.main()