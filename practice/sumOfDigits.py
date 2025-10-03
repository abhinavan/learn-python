# Sum of Digits
# Ask the user for a positive integer and print the sum of its digits. For example,
#  if the input is 1234, print 10 (since 1+2+3+4=10).

# Add input validation
try:
    input_number = input("Enter a number \n")
    # Validate it's a positive integer
    if not input_number.isdigit():
        print("Please enter a valid positive integer.")
        exit()
    
    input_list = list(input_number)
    sum = 0
    for i in input_list:
        sum += int(i)
    print(sum)
except Exception as e:
    print("An error occurred:", e)
