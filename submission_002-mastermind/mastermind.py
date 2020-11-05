import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    
    #step 1 - Generate a random code that contains four numbers then output a statement saying code has been set and number of guesses theyve got to break the code.
    
    random_code = []
    while len(random_code) < 4:
        random_digit = str(random.randint(1, 8))
        if random_digit not in random_code:
            random_code.append(random_digit)
    
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    
    #step 2 - Get user input and ensure that it is only 4 numbers long and no letters, if not output "Please enter exactly 4 digits".
    
    user_input = input("Input 4 digit code: ")
    
    number_of_turns = 12
    while number_of_turns > 0:
        while len(user_input) != 4 or user_input.isdigit() == False or "9" in user_input or "0" in user_input:
            print("Please enter exactly 4 digits.")
            user_input = input("Input 4 digit code: ")
    
        correct_digit_and_place = 0
        correct_digit_not_place = 0
        
        for i in range(0,len(random_code)):
            if user_input[i] == random_code[i]:
                correct_digit_and_place += 1
        
            elif user_input[i] in random_code:
                correct_digit_not_place += 1
        
        print("Number of correct digits in correct place:     " + str(correct_digit_and_place))
        print("Number of correct digits not in correct place: " + str(correct_digit_not_place))
        
        if correct_digit_and_place == 4:
            print("Congratulations! You are a codebreaker!\nThe code was: " + str("".join(random_code)))
            break
        elif correct_digit_and_place != 4:
            number_of_turns -= 1
            print("Turns left:", str(number_of_turns))
            if number_of_turns == 0:
                print("Game over!")
                break
        user_input = input("Input 4 digit code: ")

if __name__ == "__main__":
    run_game()