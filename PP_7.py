# Practice Python Ex7 List Comprehensions
# Take a list.  Make new list with only evens. Do it in one line.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [num for num in a if num%2 == 0]
print(b)