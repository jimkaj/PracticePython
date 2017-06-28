# Practice Python Ex 13
# Print Fibonnaci sequence
try:
    n = int(input('How many Fibonnaci numbers do you want to produce? '))
except:
    print('Invalid input.  Must be integer')
    exit() 
if n == 0: 
    print('[]')
    quit()
elif n == 1:
    print('[1]')
    quit()
else:
    fib = [1,1]
    count = 2
    while count < n:
        next = fib[-1]+fib[-2]
        fib.append(next)
        count = count +1
print(fib)



