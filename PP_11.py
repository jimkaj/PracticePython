# Practice Python Ex 11
# Ask for num & determine if prime

#query for number
try:
    num = int(input('Give me a number to test for primeness: '))
except: 
    print('Invalid input. Must enter integer number')
    quit()

#get all factors    
factors = [num]
count = 1
while count <= (num/2):
    if num%count == 0: factors.append(count)
    count = count + 1
            
#Determine Primeness
factors.sort()
print('Factors of',num,'are',factors)
if len(factors) == 2: print(num,' is prime!')
else: print(num,'is not prime.')
    
