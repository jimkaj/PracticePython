#Practice Python Ex 6
# Get string and test if palindrome

word = input("Enter text to test for palindrome-ness: ")
start = 0
end = len(word) - 1

while end > start:
    if word[start] != word[end]:
        print("That's not a palindrome!")
        quit()
    start = start + 1
    end = end -1
print(word," is a palindrome!")   