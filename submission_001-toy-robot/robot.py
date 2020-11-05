# TODO: Decompose into functions

def moving_in_square(size, degrees):
    
    '''This function prints the robots movement in a square, it has the parameters size and degrees.
    This will allow us to select different parameters later in the code without having to declare all the values again'''
    
    print("Moving in a square of size "+str(size))
    for i in range(4):
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
    
def moving_in_rectangle(length, width, degrees):
    
    '''This function prints the robots movement in a rectangle'''
    
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def moving_in_circle(degrees, length):
    
    '''This function prints the robots movement in a circle, it has the parameters degress and length.
    This will allow us to select different parameters later in the code without having to declare all the values again'''
    
    print("Moving in a circle")
    for i in range(360):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def square_dancing(length):
    
    '''This function prints the robots movement in a square thrice'''
    
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        moving_in_square(20, 90)

def crop_circles():
    
    '''This function prints the robots movement in a circle'''
    
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward 20")
        moving_in_circle(1, 1)

def move():
    
    '''A better name for this function would be "all_function_movements()", this is because all parameters for each funtion is defined in "move()" '''
    
    size = 10
    degrees = 90
    moving_in_square(size, degrees)
    
    length = 20
    width = 10
    degrees = 90
    moving_in_rectangle(length, width, degrees)
    
    degrees = 1
    length = 1
    moving_in_circle(degrees, length)
    
    length = 20
    square_dancing(length)
    
    crop_circles()

def robot_start():
    move()

if __name__ == "__main__":
    robot_start()