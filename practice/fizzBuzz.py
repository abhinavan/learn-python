# FizzBuzz (with a twist)
# Write a program that prints the numbers from 1 to 100.
#  For multiples of 3 print “Fizz,” for multiples of 5 print “Buzz.”
# For numbers which are multiples of both 3 and 5 print “FizzBuzz.”
# For numbers that are prime, print “Prime.” (Order of checks: FizzBuzz > Prime > Fizz > Buzz > Number.)
def check_if_number_is_prime(i):
    count = 0
    if (i == 1):
        return True
    for e in range(2, i):
        if (i % e == 0):
            count = 1
            break
    if (count == 0):
        return True
    else:
        return False


def is_multiple_of_number(i, multiple):
    return True if i % multiple == 0 else False


for i in range(1, 101):
    if (is_multiple_of_number(i, 3) and is_multiple_of_number(i, 5)):
        print("FizzBuzz")
    elif check_if_number_is_prime(i):
        print("Prime number")
    elif (is_multiple_of_number(i, 3)):
        print("Fizz")
    elif (is_multiple_of_number(i, 5)):
        print("Buzz")
    else:
        print(i)
