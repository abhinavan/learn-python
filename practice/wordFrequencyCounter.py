# Ask the user for a paragraph of text. Print the count of each unique word,
#  sorted by frequency. (Hint: use a dictionary.)

paragraph = input("Enter a paragraph")
words = paragraph.split()
countofEachWords = {}
for word in words:
    if (word in countofEachWords):
        countofEachWords[word] += 1
    else:
        countofEachWords[word] = 1
print(countofEachWords)
