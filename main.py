from tkinter import * 
import random

root = Tk()
root.title('Guess the Number')
root.iconbitmap('icon.ico')
width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()
pos_x = int(width_screen/2 - 250)
pos_y = int(height_screen/2 - 200)
root.geometry(f'500x400+{pos_x}+{pos_y}')

attempts = 0

def easy_game():
    global attempts
    attempts = 20

def medium_game():
    global attempts
    attempts = 10

def hard_game():
    global attempts
    attempts = 5

main_page = Frame(root)

title_game = Label(main_page, text='Game \nGuess the Number', font='Arial 25 bold').grid(column=1, row=1, padx=110, pady=40)

easy_button = Button(main_page, text='Easy Mode', font='Arial 15', bg='#71c776', width=20, command=lambda: [easy_game(), start_game()]).grid(column=1, row=2)
medium_button = Button(main_page, text='Medium Mode', font='Arial 15', bg='#f5f190', width=20, command=lambda: [medium_game(), start_game()]).grid(column=1, row=3, pady=20)
hard_button = Button(main_page, text='Hard Mode', font='Arial 15', bg='#c78171', width=20, command=lambda: [hard_game(), start_game()]).grid(column=1, row=4)

main_page.pack()

second_page = Frame(root)
third_page = Frame(root)

def myClick():
    global guess, turn, attempt
    guess = int(pseudo_guess.get())
    turn += 1
    attempt = attempts -  turn
    if guess > secret_number:
        bigger_guess = Label(second_page, text='The secret number is smaller...', font='Arial 15').grid(column=1, row=4)
        attempt_text = Label(second_page, text=f'Round: {turn} \nRemain attempts: {attempt}', font='Arial 15').grid(column=1, row=5, pady=20)
    elif guess < secret_number:
        smaller_guess = Label(second_page, text='The secret number is bigger...', font='Arial 15').grid(column=1, row=4)
        attempt_text = Label(second_page, text=f'Round: {turn} \nRemain attempts: {attempt}', font='Arial 15').grid(column=1, row=5, pady=20)
    else:
        win_game()

    if attempt == 0 and guess != secret_number:
        lost_game()

def start_game():
    global guess, pseudo_guess, turn, attempt, secret_number
    secret_number = random.randrange(101)
    main_page.pack_forget()
    second_page.pack()
    turn = 0
    guess = 0
    attempt = 1

    attempt_text = Label(second_page, text=f'Round: 0 \nRemain attempts: {attempts}', font='Arial 15').grid(column=1, row=5, pady=20)
    guess_text = Label(second_page, text='Enter your guess:', font='Arial 20').grid(column=1, row=1, pady=40)
        
    pseudo_guess = Entry(second_page, width=30)
    pseudo_guess.grid(column=1, row=2)

    guess_button = Button(second_page, text='Enter', font='Arial 15 bold', command=myClick, width=10, bg='#cfd1d1')
    guess_button.grid(column=1, row=3, pady=20)

def play_again():
    third_page.pack_forget()
    main_page.pack()

def win_game():
    second_page.pack_forget()
    third_page.pack()
    win_text = Label(third_page, text='Nice guess, \nYou won!', font='Arial 30 bold').grid(column=1, row=1, pady=50)
    play_again_button = Button(third_page, text='Play Again', font='Arial 15', width=15, bg='#e3e3e3', command=play_again)
    play_again_button.grid(column=1, row=2)

def lost_game():
    second_page.pack_forget()
    third_page.pack()
    lost_text = Label(third_page, text='Close... \nbut you lost :(', font='Arial 20 bold').grid(column=1, row=1, pady=50)
    play_again_button = Button(third_page, text='Play Again', font='Arial 15', width=15, bg='#e3e3e3', command=play_again)
    play_again_button.grid(column=1, row=2)

root.mainloop()





