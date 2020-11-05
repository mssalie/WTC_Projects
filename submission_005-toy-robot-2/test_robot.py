import unittest
from unittest.mock import patch
from io import StringIO
import sys
from robot import *


class TestRobot(unittest.TestCase):

    @patch("sys.stdin", StringIO("jeff\nhardy\n"))
    def test_input_robot_name(self):
    
        '''
        This tests that the users input for the robot name is returned as it was entered.
        '''

        sys.stdout = StringIO()
        self.assertEqual(input_robot_name(), "jeff")
        self.assertEqual(input_robot_name(), "hardy")

    @patch("sys.stdin", StringIO("jump\noff\n"))
    def test_invalid_input(self):

        '''
        This tests if the user inputs an invalid command.
        '''
        
        sys.stdout = StringIO()
        get_command_input("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next? jeff: Sorry, I did not understand 'jump'.
jeff: What must I do next? ''')


    @patch("sys.stdin", StringIO("FoRwArD 10\nFORWARD 10\nforward 10\nOfF\n"))
    def test_all_case(self):

        '''
        This tests if it accepts different types of casing, camel, upper and lower.
        '''

        sys.stdout = StringIO()
        robot_command("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,20).
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,30).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO("help\noff\n"))
    def test_robot_help_command(self):
        
        sys.stdout = StringIO()
        robot_command("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - Moves robot forward
BACK - Moves robot back
RIGHT - Changes the robots direction to the right
LEFT - Changes the robots direction to the left
jeff: What must I do next? jeff: Shutting down..
''')

    @patch("sys.stdin", StringIO("forward 20\noff\n"))
    def test_robot_command_forward(self):
        
        '''
        This tests if the robot moves forward and if it stores the correct position if users inputs "forward"
        '''

        sys.stdout = StringIO()
        robot_command("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next?  > jeff moved forward by 20 steps.
 > jeff now at position (0,20).
jeff: What must I do next? jeff: Shutting down..
''')

    @patch("sys.stdin", StringIO("back 20\noff\n"))
    def test_robot_move_back(self):

        '''
        This tests if the robot moves forward and if it stores the correct position if users inputs "forward"
        '''

        sys.stdout = StringIO()
        robot_command("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next?  > jeff moved back by 20 steps.
 > jeff now at position (0,-20).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO('''forward 10\nright\nforward 10\nright\nforward 20
right\nforward 20\nright\nforward 20\noff\n'''))
    def test_robot_turn_right(self):
        
        '''
        This tests if the direction changes when user inputs "right" as a command.
        It also checks if it updates the correct positions if they then move forward.
        '''

        sys.stdout = StringIO()
        robot_command("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff turned right.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (10,10).
jeff: What must I do next?  > jeff turned right.
 > jeff now at position (10,10).
jeff: What must I do next?  > jeff moved forward by 20 steps.
 > jeff now at position (10,-10).
jeff: What must I do next?  > jeff turned right.
 > jeff now at position (10,-10).
jeff: What must I do next?  > jeff moved forward by 20 steps.
 > jeff now at position (-10,-10).
jeff: What must I do next?  > jeff turned right.
 > jeff now at position (-10,-10).
jeff: What must I do next?  > jeff moved forward by 20 steps.
 > jeff now at position (-10,10).
jeff: What must I do next? jeff: Shutting down..
''')

    @patch("sys.stdin", StringIO('''forward 10\nleft\nforward 10\nleft\nforward 20
left\nforward 20\nleft\nforward 20\noff\n'''))
    def test_robot_turn_left(self):

        '''
        This tests if the direction changes when user inputs "left" as a command.
        It also checks if it updates the correct positions if they then move forward.
        '''

        sys.stdout = StringIO()
        robot_command("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff turned left.
 > jeff now at position (0,10).
jeff: What must I do next?  > jeff moved forward by 10 steps.
 > jeff now at position (-10,10).
jeff: What must I do next?  > jeff turned left.
 > jeff now at position (-10,10).
jeff: What must I do next?  > jeff moved forward by 20 steps.
 > jeff now at position (-10,-10).
jeff: What must I do next?  > jeff turned left.
 > jeff now at position (-10,-10).
jeff: What must I do next?  > jeff moved forward by 20 steps.
 > jeff now at position (10,-10).
jeff: What must I do next?  > jeff turned left.
 > jeff now at position (10,-10).
jeff: What must I do next?  > jeff moved forward by 20 steps.
 > jeff now at position (10,10).
jeff: What must I do next? jeff: Shutting down..
''')


    @patch("sys.stdin", StringIO('''forward 210\nright\nforward 110\nright
forward 210\nright\nforward 110\noff\n'''))
    def test_robot_out_of_bounds(self):
        
        '''
        This tests that the robot can only move where x >= -100 and x <= 100 and y >= -200 and y <= 200.
        '''

        sys.stdout = StringIO()
        robot_command("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next? jeff: Sorry, I cannot go outside my safe zone.
 > jeff now at position (0,0).
jeff: What must I do next?  > jeff turned right.
 > jeff now at position (0,0).
jeff: What must I do next? jeff: Sorry, I cannot go outside my safe zone.
 > jeff now at position (0,0).
jeff: What must I do next?  > jeff turned right.
 > jeff now at position (0,0).
jeff: What must I do next? jeff: Sorry, I cannot go outside my safe zone.
 > jeff now at position (0,0).
jeff: What must I do next?  > jeff turned right.
 > jeff now at position (0,0).
jeff: What must I do next? jeff: Sorry, I cannot go outside my safe zone.
 > jeff now at position (0,0).
jeff: What must I do next? jeff: Shutting down..
''')

    @patch("sys.stdin", StringIO("sprint 5\noff\n"))
    def test_robot_sprint_command(self):

        '''
        This tests the robot prints the amount of steps it moved forward by -1 everytime. 
        Until it reaches 0 then it displays the current position and asks for user input again.
        '''

        sys.stdout = StringIO()
        robot_command("jeff")
        self.assertEqual(sys.stdout.getvalue(), '''jeff: What must I do next?  > jeff moved forward by 5 steps.
 > jeff moved forward by 4 steps.
 > jeff moved forward by 3 steps.
 > jeff moved forward by 2 steps.
 > jeff moved forward by 1 steps.
 > jeff now at position (0,15).
jeff: What must I do next? jeff: Shutting down..
''')


if __name__ == "__main__":
    unittest.main()







