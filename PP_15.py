# Practice Python Ex 15
# enter long string, print back in reverse order

# this does it in one line: ' '.join(inp.split()[::-1])
 

def text_rev(inp):
    sinp = inp.split()
    count = len(sinp)
    rinp = str()
    while count > 0:
        count = count -1
        rinp = rinp + sinp[count] + ' ' 
    return rinp    
    
x = input('Enter a bunch of words: ')
answer = text_rev(x)
print(answer)
     