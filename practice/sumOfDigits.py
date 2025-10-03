# Sum of Digits
# Ask the user for a positive integer and print the sum of its digits. For example,
#  if the input is 1234, print 10 (since 1+2+3+4=10).
input_number = input("Enter a number \n")
input_list = list(input_number)
sum = 0
for i in input_list:
    sum += int(i)
print(sum)
