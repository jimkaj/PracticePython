# PP #3
# take a list and print elements less than 5
#lst = list()
#while True:
#    x = input("Enter a number or type 'done': ")
#    if x == 'done': break
#    try: x = int(x)
#    except: 
#        print("That's not a valid entry")
#        break
#    if x < 5:
#        lst.append(x)
#print('These numbers were less than 5: ', lst)        

#in one line:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
    if num < 5: print(num)