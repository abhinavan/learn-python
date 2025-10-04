# Write a function that takes a string and returns True if it’s a palindrome (the same forwards and backwards),
# ignoring spaces and case.
inputString = input("Enter a word to check for palindrome \n")
inputString = inputString.lower().strip()
reversed_string = inputString[::-1]
if (inputString == reversed_string):
    print("String is palindrome")
else:
    print("String is not a palindrome")
print("Palindrome" if inputString == reversed_string else "Not a palindrome")
