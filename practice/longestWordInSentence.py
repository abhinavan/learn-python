# Write a program that asks the user for a sentence, then prints the length (number of letters) of the longest word.
#  (Tip: Use split() to break the sentence into words.)

sentence = input("Enter a sentence")
words = sentence.split(" ")
max_length = 0
resulting_word = ''
for index, value in enumerate(words):
    if (len(value) > max_length):
        max_length = len(value)
        resulting_word = value
print(resulting_word)
