# Practice Python Ex10
#  Take two lists.  identify shared items. Use list comprehensions.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
shared = [num for num in a if num in b]

#eliminate duplicates
result = []
for num in shared:
    if num not in result: result.append(num) 
print("Shared numbers are ",result)        

