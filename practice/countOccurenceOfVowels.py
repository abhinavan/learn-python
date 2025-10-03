# Count Vowels in a String
# Ask the user for a word or sentence and print how many vowels (a, e, i, o, u) it contains.

sentence = input("Enter a sentence ")
# Handle uppercase vowels by including them in the list
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
characters = list(sentence)
print(characters)
count = 0
for i in characters:
    if (i in vowels):
        count += 1
print(count)
