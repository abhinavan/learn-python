# Count Vowels in a String
# Ask the user for a word or sentence and print how many vowels (a, e, i, o, u) it contains.

sentence = input("Enter a sentence ")
vowels = ['a', 'e', 'i', 'o', 'u']
characters = list(sentence)
print(characters)
count = 0
for i in characters:
    if (i in vowels):
        count += 1
print(count)
