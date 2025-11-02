# Write a program that asks the user for a sentence, then prints the length (number of letters) of the longest word.
#  (Tip: Use split() to break the sentence into words.)

sentence = input("Enter a sentence")
words = sentence.split(" ")
max_length = 0
# Extended: Store all words with the longest length (handle ties)
resulting_words = []

for index, value in enumerate(words):
    if (len(value) > max_length):
        max_length = len(value)
        resulting_words = [value]  # Reset list with new longest word
    elif (len(value) == max_length and len(value) > 0):
        resulting_words.append(value)  # Add to list if tied

print("Longest word(s):", resulting_words)
