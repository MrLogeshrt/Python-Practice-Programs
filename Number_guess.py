#Guess a random number game program


import random
r = random.randint(0,10)
i = 0
c = 5
tot = 0
while i < 5 :
    while True :
        n = int(input("Enter your guess b/w 0 to 10 : "))
        if n > 10 or n < 0 :
            print("Your guess sholud be b/w 0 to 10 ..")
        else :
            break
    if n == r :
        print("You guessed the correct number..!")
        tot += 1
        c -= 1
        break
    elif n > r :
        print("Your guess is 'Too High..'" )
        c -= 1
        print(f"You have {c} guesses remaining")
    else :
        print("your guess is 'Too Low..'")
        c -= 1
        print(f"You have {c} guesses remaining")
    i += 1
if tot == 0 :
    print("You're out of chances.. Better luck next time ")
else :
    print(f"your score is {tot}..")
    
    