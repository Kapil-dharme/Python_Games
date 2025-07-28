import random
import string
print("This tool generates a strong password . ")
passw=string.ascii_letters+string.punctuation+string.digits
press=int(input("To generate password please press 1."))
if press==1:
    pass_len=int(input("Enter the length of the password : "))
    print("Password :-")
    for val in range (1,pass_len+1):
        passq=random.choice(passw)
        print(passq,end="")

