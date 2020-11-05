# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay']
# variables tracking position and direction

position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
# area limit vars

min_y, max_y = -200, 200
min_x, max_x = -100, 100

# empty list where all commands gets added to, to recall later
history_list = []

# boolean to print output if True do not print output
silent = False

#boolean to print output in reverse 
reverse = False

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):

    global history_list, silent, reverse
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    Checks silent and reverse flags
    """
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    store_command = command

    command = silent_and_reversed(command)

    while len(command) == 0 or not valid_command(command):
        silent = False
        reverse = False

        output(robot_name, "Sorry, I did not understand '"+store_command+"'.")

        command = input(prompt)
        store_command = command
        command = silent_and_reversed(command)
    
    store_history(command)
    return command.lower()

    
def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1].split('-')
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    if it is not an int then return False.
    else return True
    """
    
    check_is_int = list(map(lambda var: var.isdigit(), value))
    if False in check_is_int:
        return False
    return True


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    (command_name, arg1) = split_command_input(command)
    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - makes the robot replay all previous commands
REPLAY SILENT - makes the robot replay all previous commands silently
REPLAY REVERSED - makes the robot replay all previous commands in reverse
REPLAY REVERSED SILENT - makes the robot replay all previous commands in reverse silently
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y
    new_x = position_x
    new_y = position_y
    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def store_history(command):
    """
    Stores all previous input except for off, help and replay
    """
    global history_list

    move_list = ['forward', 'back', 'right', 'left', 'sprint']
    (command_name, arg1) = split_command_input(command)
    while command_name in move_list:
        history_list.append(command)
        return history_list

    return history_list


def replay_command(robot_name,n):
    """
    Makes the robot replay all previous commands
    """
    global history_list

    replay_counter = 0

    if len(n) > 1:
        for action in history_list[len(history_list) - int(n[0]) : len(history_list)- int(n[1])]:
            handle_command(robot_name, action)
            replay_counter += 1

    elif len(n) == 1:
        for action in history_list[len(history_list) - int(n[0]):]:
            handle_command(robot_name, action)
            replay_counter += 1

    else:
        for action in history_list:
            handle_command(robot_name, action)
            replay_counter += 1


    return True, ' > ' + robot_name + ' replayed ' + str(replay_counter) + ' commands.'


def silent_replay_command(robot_name,n):
    """
    makes the robot replay all previous commands silently
    """
    global history_list, silent

    replay_counter = 0

    if len(n) > 1:
        for action in history_list[len(history_list) - int(n[0]) : len(history_list)- int(n[1])]:
            silent = True
            handle_command(robot_name, action)
            replay_counter += 1

    elif len(n) == 1:
        for action in history_list[len(history_list) - int(n[0]):]:
            silent = True
            handle_command(robot_name, action)
            replay_counter += 1

    else:
        for action in history_list:
            silent = True
            handle_command(robot_name, action)
            replay_counter += 1
        
    silent = False
    return True, ' > ' + robot_name + ' replayed ' + str(replay_counter) + ' commands silently.'


def replay_reversed(robot_name,n):
    """
    makes the robot replay all previous commands in reverse
    """
    global history_list

    replay_counter = 0
    history_list = history_list[::-1]
    if len(n) > 1:
        for action in history_list[len(history_list) - int(n[0]) : len(history_list)- int(n[1])]:
            handle_command(robot_name, action)
            replay_counter += 1

    elif len(n) == 1:
        for action in history_list[len(history_list) - int(n[0]):]:
            handle_command(robot_name, action)
            replay_counter += 1

    else:
        for action in history_list:
            handle_command(robot_name, action)
            replay_counter += 1

    reverse = False
    return True, ' > ' + robot_name + ' replayed ' + str(replay_counter) + ' commands in reverse.'


def replay_reversed_silent(robot_name, n):
    """
    makes the robot replay all previous commands in reverse silently
    """

    global history_list, silent
    replay_counter = 0
    history_list = history_list[::-1]

    if len(n) > 1:
        for action in history_list[len(history_list) - int(n[0]) : len(history_list)- int(n[1])]:
            silent = True
            handle_command(robot_name, action)
            replay_counter += 1

    elif len(n) == 1:
        for action in history_list[len(history_list) - int(n[0]):]:
            silent = True
            handle_command(robot_name, action)
            replay_counter += 1

    else:
        for action in history_list:
            silent = True
            handle_command(robot_name, action)
            replay_counter += 1

    
    silent = False
    reverse = False
    return True, ' > ' + robot_name + ' replayed ' + str(replay_counter) + ' commands in reverse silently.'
    

def silent_and_reversed(command):
    
    """
    This function replaces the silent or reverse if it is in the command with an empty string.
    I did this so that 'replay' can be used again with other input.
    """
    global silent, reverse

    if ' silent' in command:
        command = command.replace(' silent', '')
        silent = True
    
    if ' SILENT' in command:
        command = command.replace(' SILENT', '')
        silent = True

    if ' reversed' in command:
        command = command.replace(' reversed', '')
        reverse = True

    if ' REVERSED' in command:
        command = command.replace(' REVERSED', '')
        reverse = True

    return command


def all_replay_commands(robot_name, n):

    """
    This function calls other specific functions depending on if the silent and reverse flags are True or False.
    I silent flag is True it will only output position and if reverse flag is True it will output in reverse,
    otherwise if Flags are False it will output normally.
    """
    global history_list, silent, reverse

    if silent == False and reverse == False:
        (do_next, output) = replay_command(robot_name, n)

    elif silent == True and reverse == False:
        (do_next, output) = silent_replay_command(robot_name, n)

    elif silent == False and reverse == True:
        (do_next, output) = replay_reversed(robot_name, n)

    elif silent == True and reverse == True:
        (do_next, output) = replay_reversed_silent(robot_name, n)

    return True, output


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)
    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg[0]))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg[0]))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg[0]))
    elif command_name == 'replay':
        (do_next, command_output) = all_replay_commands(robot_name, arg)
    
    if silent == False:
        print(command_output)
        show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""
    global position_x, position_y, current_direction_index, history_list, silent, reverse
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    history_list = []
    silent = False
    reverse = False
    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()