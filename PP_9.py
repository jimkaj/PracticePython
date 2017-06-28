# Practice Python #9
# Generate random number from 1-9, have use guess number
import random
num = random.randrange(1,10,1)
print('I have selected a number between 1 and 9')
print("Type 'exit' to stop playing")
count = 0

while True:
    guess = input("What number have I selected? ")
    if guess == 'exit':
        break
    count = count + 1
    try: guess = int(guess)
    except:
        print("Invalid Input. You must input an integer or 'exit' to quit playing")
        count = count -1
        continue
        
    if guess == num: 
        print('You guessed it! That took you',count,'tries')
        exit()
    if guess < num:
        print('Too low! Guess again.')
    if guess > num:
        print('Too high! Guess again.')
        
    
    