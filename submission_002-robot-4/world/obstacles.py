import turtle
import random

# empty list to which obsticles positions are appended to.
obstacles_list = []

def is_position_blocked(x, y):

    '''
    This function checks if there is an obsticle in a certain position. 
    If position is blocked return True else return False.
    '''

    global obstacles_list

    for i in obstacles_list:
        if x >= i[0] and x <= i[0] + 4 and y >= i[1] and y <= i[1] + 4:
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    
    '''
    This function checks if the robot can move on a certain path.
    If path is blocked return True else return False.
    '''
    
    global obstacles_list

    if x1 > x2:
        x1, x2 = x2, x1
    
    if y1 > y2:
        y1, y2 = y2, y1

    if y1 == y2:
        for x in range(x1, x2 + 1):
            if is_position_blocked(x, y1):
                return True

    if x1 == x2:
        for y in range(y1, y2 + 1):
            if is_position_blocked(x1, y):
                return True

    return False


def get_obstacles():

    '''
    This function generates the number of obsticles in the world and the obstacles positions.
    Returns the obstacle list with all positions appended.
    '''

    global obstacles_list
    
    for i in range(random.randint(0,10)):

        x = random.randint(-100,100)
        y = random.randint(-200,200)
        obs = (x,y)
        obstacles_list.append(obs)

    return obstacles_list