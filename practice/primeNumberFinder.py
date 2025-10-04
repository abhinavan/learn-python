#  Prime Number Finder
# Ask the user for a number N. Print all prime numbers between 2 and N, inclusive. Try to make your solution efficient.
input_number = int(input("Enter a number to be checked for prime"))
count = 0
if (input_number == 1):
    print("Prime number")
elif (input_number != 1 and input_number != 0):
    for i in range(2, input_number):
        if (input_number % i == 0):
            print("Not a prime number")
            count = 1
            break
if (count == 0):
    print("Prime number")
