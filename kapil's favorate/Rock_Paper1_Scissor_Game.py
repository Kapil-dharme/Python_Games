import random
ask=input("Please press 'Enter Key' to start the Game.")
if ask=="":
    print("The properties of game are:-\npress 1 for Rock\npress 2 for Paper.\npress 3 for Scissors.")
Rock=1
Paper=2
scissors=3
#Game starts
while True:
    while True:
        #user's choice.
        choice=int(input("Enter your choice :-"))
        if choice==1:
            print("Your choice = Rock 🪨.")
            break
        elif choice==2:
            print("Your choice = Paper 📃.")
            break
        elif choice==3:
            print("Your choice = Scissors ✂️.")
            break
        else:
            print("You have chosen a wrong choice.\nplease choose correct one.")
            continue
    #computer choice.
    print("Its time for computer to make a choice.\nThinking...🤔")
    comchoice=random.randint(1,3)
    if comchoice==1:
        print("Computer choice = Rock 🪨.")
    elif comchoice==2:
        print("Computer choice = Paper 📃.")
    else :
        print("Computer choice = Scissors ✂️.")
    #printing results.   
    print("RESULTS :-")
    if comchoice==choice:
        print("Its a Draw.")
    elif comchoice==1 and choice==2:
        print("YOU WIN.")
    elif comchoice==2 and choice==1:
        print("YOU LOSE.")
    elif comchoice==1 and choice==3:
        print("YOU LOSE.")
    elif comchoice==3 and choice==1:
        print("YOU WIN.")
    elif comchoice==2 and choice==3: 
        print("YOU WIN.")
    else:
        print("YOU LOSE.")
    print("___GAME OVER___")
    press=int(input("If you want to play again then please press 5.\nTo Quit the game press 8."))
    if press==5:
        continue
    elif press==8:
        print("You QUIT the Game.")
        break
    else:
        print("Please enter a valid choice.")
        continue