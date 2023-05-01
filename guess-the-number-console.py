import random

def game():
    play_again = 'yes'
    score = 0
    while play_again in 'yes, Yes, YES':
        level = int(input('-------------------------------------------------- \n                    Levels: \n-------------------------------------------------- \n                  (1) - Easy \n                  (2) - Medium \n                  (3) - Hard \n-------------------------------------------------- \n     Enter the number according to the level: '))
        print('--------------------------------------------------')
        while level != 1 and level != 2 and level != 3:
            level = int(input('-------------------------------------------------- \n       Invalid. Enter again: '))
        if level == 1:
            attempts = 20
        elif level == 2:
            attempts = 10
        else:
            attempts = 5
        secret_number = int(random.randrange(101))
        guess = 101
        turn = 0
        attempt = 1
        while attempt != 0:
            guess = int(input('     Enter your guess: '))
            turn += 1
            attempt = attempts - turn
            if guess == secret_number:
                break
            if guess > secret_number:
                print(f'-------------------------------------------------- \n You are in turn {turn}. You have more {attempt} attempts. \n \n          The number should be smaller... \n--------------------------------------------------')
            elif guess < secret_number:
                print(f'-------------------------------------------------- \n You are in turn {turn}. You have more {attempt} attempts. \n \n          The number should be bigger... \n--------------------------------------------------')
        if guess == secret_number:
            score += 1
            print(f'     You won, Congratulations!     Current Score: {score} \n--------------------------------------------------')
        if attempt == 0:
            #score -= 1
            if score > 1:
                score -= 1
            print(f'     You lost :(     Current Score: {score} \n--------------------------------------------------')
            print(f'            The secret number was {secret_number}.')
        play_again = input('Try again? (yes or no)? ')
        while play_again not in 'yes, Yes, YES, no, No, NO':
            play_again = input('-------------------------------------------------- \n               Invalid. \nTry again? (yes or no)? ')
    print('-------------------------------------------------- \n               See you next time! \n--------------------------------------------------')
game()


