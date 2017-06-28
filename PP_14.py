# Practice Python Ex 14
# Write a function that takes a list and returns new list minus duplicates

#Enter List


def EnterList()
    lst = list()
    while True:
        try:
            inp = int(input('Enter a number or type "done"'))
            lst.append(inp)
        except: 
            break
    return lst        


#Eliminate duplicates
nlst = list()
for n in lst:
    if n not in nlst:
        nlst.append(n)  
print('New List: ',nlst)  

    