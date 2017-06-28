# Practice Python Ex 11
# Look for primes

#input range of numbers to test
print('What range of numbers do you want to test for primes?')
try:
    num = int(input('Starting number of range: '))
    max = int(input('Last number of range: '))
except: 
    print('Invalid range.  You must enter integer numbers.')
    quit()

#loop through and find primes
primes = [1]
while num < max:
    #find at least 3 factors    
    factors = [num]
    count = 1
    while count <= (num/2):
        if num%count == 0: factors.append(count)
        count = count + 1
        if len(factors) > 2: break
   
        
    #Determine Primeness
    if len(factors) == 2: primes.append(num)
    num = num +1
print('Primes are: ',primes)
    