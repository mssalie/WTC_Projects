
x = 0
y = 0

def robot_start():
    """This is the entry function, do not change"""
    robot_name = input_robot_name()
    robot_command(robot_name)


def input_robot_name():

    '''
    This function gets the users input for the robots name.
    It returns "robot_name" to be used later.
    '''

    robot_name = input("What do you want to name your robot? ")
    print(robot_name + ": Hello kiddo!")
    return robot_name


def get_command_input(robot_name):

    '''
    This function asks user input again if the input is not in the command list
    '''

    command_list = ["off", "help", "forward", "back", "right", "left", "sprint"]
    user_command = input(robot_name + ": What must I do next? ")

    while user_command == "" or user_command.split()[0].lower() not in command_list:
        print(robot_name + ": Sorry, I did not understand", "'" + user_command + "'.")
        user_command = input(robot_name + ": What must I do next? ")
    
    return user_command


def robot_help_command(user_command):

    '''
    This function stores the help list and returns the list.
    '''

    help_list = [
    "OFF  - Shut down robot",
    "HELP - provide information about commands",
    "FORWARD - Moves robot forward",
    "BACK - Moves robot back",
    "RIGHT - Changes the robots direction to the right",
    "LEFT - Changes the robots direction to the left"
    ]
    
    return help_list


def print_help_list(help_list):

    '''
    This function prints the help list.
    '''

    print("I can understand these commands:")
    for i in help_list:
        print(i)


def robot_off_command(robot_name):

    '''
    This function prints "Shutting down.." if user inputs off.
    It also resets the x and y values back to 0.
    '''
    global x
    global y
    
    print(robot_name + ": Shutting down..")

    x = 0
    y = 0


def robot_move_forward(robot_name, user_command, default_direction):

    '''
    This function puts restrictions on the move forward command.
    It prints how many steps the robot moved forward by.
    It prints the current position of the robot.
    '''

    global x
    global y

    steps = user_command.split()[1]
    
    if default_direction == "up":
        if y + int(steps) > 200:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
        else:
            y += int(steps)
            print(" >", robot_name, "moved forward by", int(steps), "steps.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
    
    elif default_direction == "right":
        if x + int(steps) > 100:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
        else:    
            x += int(steps)
            print(" >", robot_name, "moved forward by", int(steps), "steps.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
    
    elif default_direction == "down":
        if y - int(steps) < -200:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
        else:
            y -= int(steps)
            print(" >", robot_name, "moved forward by", int(steps), "steps.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
    
    elif default_direction == "left":
        if x - int(steps) < -100:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
        else:
            x -= int(steps)
            print(" >", robot_name, "moved forward by", int(steps), "steps.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")


def robot_move_back(robot_name, user_command, default_direction):

    '''
    This function puts restrictions on the move back command.
    It prints how many steps the robot moved back by.
    It prints the current position of the robot.
    '''

    global x
    global y
    steps = user_command.split()[1]

    if default_direction == "up":
        if y - int(steps) < -200:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
        else:
            y -= int(steps)
            print(" >", robot_name, "moved back by", steps, "steps.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")

        
    elif default_direction == "right":
        if x - int(steps) < -100:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
        else:
            x -= int(steps)
        print(" >", robot_name, "moved back by", steps, "steps.")
        print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")

    
    elif default_direction == "down":
        if y + int(steps) > 200:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
        else:
            y += int(steps)
            print(" >", robot_name, "moved back by", steps, "steps.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")


    elif default_direction == "left":
        if x + int(steps) > 100:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
        else:
            x += int(steps)
            print(" >", robot_name, "moved back by", steps, "steps.")
            print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")


def robot_turn_right(robot_name, user_command, default_direction):


    '''
    This function changes the direction of the robot when user inputs "right".
    '''

    global x
    global y

    if default_direction == "up" and user_command == "right":
        default_direction = "right"
        print(" >", robot_name, "turned right.")
        print(" >", robot_name, "now at position","("+ str(x) + "," + str(y) +")" + ".")

    elif default_direction == "right" and user_command == "right":
        default_direction = "down"
        print(" >", robot_name, "turned right.")
        print(" >", robot_name, "now at position","("+ str(x) + "," + str(y) +")" + ".")

    elif default_direction == "down" and user_command == "right":
        default_direction = "left"
        print(" >", robot_name, "turned right.")
        print(" >", robot_name, "now at position","("+ str(x) + "," + str(y) +")" + ".")

    elif default_direction == "left" and user_command == "right":
        default_direction = "up"
        print(" >", robot_name, "turned right.")
        print(" >", robot_name, "now at position","("+ str(x) + "," + str(y) +")" + ".")
    
    return default_direction


def robot_turn_left(robot_name, user_command, default_direction):

    '''
    This function changes the direction of the robot when user inputs "left".
    '''

    global x
    global y

    if default_direction == "up" and user_command == "left":
        default_direction = "left"
        print(" >", robot_name, "turned left.")
        print(" >", robot_name, "now at position","("+ str(x) + "," + str(y) +")" + ".")

    elif default_direction == "left" and user_command == "left":
        default_direction = "down"
        print(" >", robot_name, "turned left.")
        print(" >", robot_name, "now at position","("+ str(x) + "," + str(y) +")" + ".")

    elif default_direction == "down" and user_command == "left":
        default_direction = "right"
        print(" >", robot_name, "turned left.")
        print(" >", robot_name, "now at position","("+ str(x) + "," + str(y) +")" + ".")

    elif default_direction == "right" and user_command == "left":
        default_direction = "up"
        print(" >", robot_name, "turned left.")
        print(" >", robot_name, "now at position","("+ str(x) + "," + str(y) +")" + ".")

    return default_direction


def robot_sprint(robot_name, user_command, default_direction, steps):


    '''
    This function puts restrictions on the sprint command.
    It prints how many steps the robot moved recursively.
    It prints the current position of the robot.
    '''

    global x
    global y

    if steps == 0:
        print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
    else:
        if default_direction == "up":
            if y + int(steps) > 200:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
            else:
                y += int(steps)
                print(" >", robot_name, "moved forward by", int(steps), "steps.")
                robot_sprint(robot_name, user_command, default_direction,steps - 1)
            
        elif default_direction == "right":
            if x + int(steps) > 100:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
            else:    
                x += int(steps)
                print(" >", robot_name, "moved forward by", int(steps), "steps.")
                robot_sprint(robot_name, user_command, default_direction,steps - 1)

        elif default_direction == "down":
            if y - int(steps) < -200:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
            else:
                y -= int(steps)
                print(" >", robot_name, "moved forward by", int(steps), "steps.")
                robot_sprint(robot_name, user_command, default_direction,steps - 1)
        
        elif default_direction == "left":
            if x - int(steps) < -100:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                print(" >", robot_name, "now at position", "(" + str(x) + ","+ str(y) + ")" + ".")
            else:
                x -= int(steps)
                print(" >", robot_name, "moved forward by", int(steps), "steps.")
                robot_sprint(robot_name, user_command, default_direction,steps - 1)


def robot_command(robot_name):

    '''
    This function sets robot direction as up.
    It calls function based on user input.
    It keeps on running until the user inputs "off".
    '''
    
    global x
    global y

    default_direction = "up"
    correct = False
    while not correct:
        user_command = get_command_input(robot_name)
        
        if len(user_command.split()) == 1:
            if user_command.split()[0].lower() == "help":
                help_list = robot_help_command(user_command)
                print_help_list(help_list)
            
            elif user_command.split()[0].lower() == "off":
                robot_off_command(robot_name)
                break

            elif user_command.split()[0].lower() == "right":
                default_direction = robot_turn_right(robot_name, user_command, default_direction)

            elif user_command.split()[0].lower() == "left":
                default_direction = robot_turn_left(robot_name, user_command, default_direction)

        if len(user_command.split()) == 2:
            if user_command.split()[0].lower() == "forward":
                robot_move_forward(robot_name, user_command, default_direction)

            elif user_command.split()[0].lower() == "back":
                robot_move_back(robot_name, user_command, default_direction)

            elif user_command.split()[0].lower() == "sprint":
                steps = int(user_command.split()[1])
                robot_sprint(robot_name, user_command, default_direction, steps)


if __name__ == "__main__":
    robot_start()