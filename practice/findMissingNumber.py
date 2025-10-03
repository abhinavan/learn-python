# Find the Missing Number
# Given a list of numbers from 1 to N (ask the user for these numbers, but leave out one),
# find and print the missing number. For example, if the user enters 2, 5, 1, 4, 3, 7, 6, 8, 10,
#  print out 9 (since it’s missing).

input_numbers = input("provide list of numbers \n")
limit = int(input("Enter max number till where you want the numbers \n"))
inputList = list(map(int, input_numbers.split(",")))
output = list()
for i in range(limit):
    if (i not in inputList):
        output.append(i)
print(output)
