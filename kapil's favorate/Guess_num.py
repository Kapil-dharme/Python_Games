import random
print("In this Game a target is randomly generated . You just have to guess that target.")
while True:
    target=random.randint(1,100)
    press=int(input("Press 1 to enter the Game."))
    if press==1 :
        while True:
            guess=int(input("Enter your guess : "))
            if (guess>target):
                print("Your guess is big , please guess small.")
                continue
            elif (guess<target):
                print("Your guess is small , please guess big.")
                continue
            else:
                print("Your guess is correct .\nYou won the game.")
                print("___GAME OVER___")
                p=input("To play again please press 2.")
                if(p==2):
                    continue
    else :
        print("Please enter the valid argument.")
        continue