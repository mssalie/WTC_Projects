import random

# TODO: Decompose into functions

code = [0,0,0,0]
answer = ("")
correct_digits_and_position = 0
correct_digits_only = 0
turns = 0
correct = ("")

def randomly_generate_code():
    
    '''The only things this function does is generate a random 4 number code and prints a message to the user. We do not need any parameters at this point.'''
    
    global code
    code = [0,0,0,0]
    
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def get_user_input():
    
    '''The only things this function does is get the users input. We do not need any parameters at this point.'''
    
    global answer
    
    answer = input("Input 4 digit code: ")
    if len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        get_user_input()


def print_result():
    
    '''This function prints the result of the user's guess.'''
    
    global turns
    global correct_digits_and_position
    global correct_digits_only
    
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    turns += 1


def check_result():
    
    '''This function allows the us to check the result of the user's guess.'''
    
    global code
    global answer
    global correct_digits_and_position
    global correct_digits_only
    
    correct_digits_and_position = 0
    correct_digits_only = 0
    
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    
    print_result()


def win_lose_condition():
    
    '''
    This function breaks the loop to ask for user input if the users input is correct.
    If it isnt correct and all the users turns are used we will then end the game.
    '''
    
    global turns
    global correct
    global correct_digits_and_position
    
    correct = False
    
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))


def show_the_code():
    
    global code
    
    print('The code was: '+str(code))


def run_game():
    
    '''This function creates the loop for the entire code so that it runs as it should and it calls all other functions.'''
    
    global correct
    correct = False
    
    randomly_generate_code()
    
    while not correct and turns < 12:
        get_user_input()
        check_result()
        win_lose_condition()
    show_the_code()
    
if __name__ == "__main__":
    run_game()