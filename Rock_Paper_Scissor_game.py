#Rock Paper Scissor Game Program..
import random
choice = ['rock', 'paper', 'scissor']

cs = 0 
us = 0

def user_input():
    inp = input("Enter you choice : ")
    input_user = inp.lower()
    if input_user not in choice:
        print("Invalid choice! Please enter rock, paper or scissor.")
        user_input()
    return input_user

    return input_user

def computer_score():
    global cs
    cs = cs + 1 

def user_score():
    global us
    us = us + 1

def score():
    global us,cs
    print(f"Your Score : {us} \t Computer Score : {cs}")

def wish():
    ch = int(input("Do you want to continue (1/0): "))
    return ch


while True :
    n = random.randint(0,2)
    computer_choice = choice[n]
    ip = user_input()
    print(f"Computer's Choise : {computer_choice}")
    if ip == computer_choice:
        print("It's a draw!")
    elif ((ip == 'rock') and (computer_choice == 'paper')) or ((ip == 'scissor') and (computer_choice == 'rock')) or ((ip == 'paper') and (computer_choice == 'scissor')):
        computer_score()
    else :
        user_score()
    score()
    c = wish()
    if c != 1 :
        if us == cs :
            print(f"The Final Result of the game is : DRAW..!")
        elif us > cs :
            print(f"The Final Result of the game is : YOU WIN..!")
        else :
            print(f"The Final Result of the game is : COMPUTER WIN..! \nBetter luck next time..")
        break
