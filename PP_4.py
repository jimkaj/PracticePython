# Practice Python #4
# ask for number and print list of divisors
try:
    num = int(input("Give me an integer number you wanker: "))
except:
    print("That's not an integer number you melvin.")
    quit()
count = num 
div = list()
while count > 0:
    if num%count == 0:
        div.append(count)
    count = count - 1
print('The divisors for',num,'are',div)
    