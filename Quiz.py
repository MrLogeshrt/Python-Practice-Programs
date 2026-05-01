#Quiz game program


import random
print("Welcome to the Quiz 😎..!\n")
d = {
    "Who is known as the 'Father of the Nation' in India?": "Mahatma Gandhi",
    "What is the capital city of Japan?": "Tokyo",
    "Which planet is known as the 'Red Planet'?": "Mars",
    "Who invented the light bulb?": "Thomas Alva Edison",
    "What is the largest ocean in the world?": "Pacific",
    "Which country is known as the Land of the Rising Sun?": "Japan",
    "What is the currency of the United Kingdom?": "Pound",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "Which is the longest river in the world?": "Nile",
    "What gas do plants absorb from the atmosphere?": "Carbon Dioxide"
}

def quiz(d) :
    ran = random.sample(list(d.keys()),len(d))
    tot = 0
    i=1
    for question in ran :
        print(f"Question {i} : {question}")
        ans = input("Enter your Answer : ").strip().lower()
        answer = d[question].strip().lower()
        if ans == answer :
            print("✅ Correct answer..!")
            tot += 1
        else :
            print("❌ Wrong answer.")
        i += 1
    return tot

def result(tot) :
    if tot == 10  :
        print(f"Fantastic 🤩.. You got all right ..! 🎯 Your Score is {tot}")
    elif tot < 10 and tot > 5 :
        print(f"Great 😎.. 🎯 Your Score is {tot} ")
    elif tot > 0 and tot < 6 :
        print(f"Good Try 😊.. 🎯 Your Score is {tot}")
    else :
        print(f"Better luck next time 😔.. 🎯 Your Score is {tot}")
    



while True :
    ch = input("Are you ready to play 😊 ..? (y/n): ")
    if ch not in "yn" :
        print("Invalid choice.")
    elif ch == "y" :
        print("\nGreat👍.. \nLet's start..\n")
        q = quiz(d)
        result(q)
    else :
        print("\nThank you for playing 🙏..!\nSee you soon..👀")
        break
