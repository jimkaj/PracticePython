# Practice Python Ex #16 Password Generator
# Create a random password.  Make it ask for easy or hard, how long
# KEY COMMANDS: ord('A')=65 and chr(65)='A'

import random

def GenEasy():
    A = ['Big','Red','Skinny','Blue','Pretty','Musical','Athletic','Sorry','Ugly','Fast','Slow','Smart','Dirty','New','Noble']
    B = ['Pursuit','Challenge','Rescue','Rooster','Cello','Elephant','Candy','Apple','Corn','Tuxedo','Butterfly','Horn','Fork','Stapler','Ant']
    P = A[(random.randint(0,14))] + B[(random.randint(0,14))] + str(random.randint(0,9999))
    return(P)

def GenHard():
    L = input('How long do you want the password to be? <enter integer number>: ')
    try: L = int(L)
    except: 
        print("You need to enter an integer number")
        quit()
    P = str() # Password
    N = str() # New character to add to password
    while L > 0:
        CT = random.randint(1,4) # Selects ASCII Character Ranges that are suitable(Symbol, Lower, Upper)
        if CT == 1: 
            N = chr(random.randint(47,57)) # ASCII for numbers
        elif CT == 2: 
            N = chr(random.randint(64,95)) #ASCII for lower and appropriate symbols
        elif CT == 3: 
            N = chr(random.randint(97,123)) #ASCII for upper and appropriate symbols
        elif CT == 4:
            N = chr(random.randint(33,43)) # ASCII for more symbols
        P = P + str(N) # appends the new character to the password
        L = L -1
    return(P)
    
print("Welcome to Password Generator")
print("Do you want to create an easy or hard password?: ")
inp = input("Type 'e' for easy or 'h' for hard:" )
if inp == "e": password = GenEasy()
elif inp == "h": password = GenHard()
else: 
    print("You need to type 'e' or 'h'")
    quit()
print("Your password is: ",password)
