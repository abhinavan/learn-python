# Basic Python Questions
# Print a Greeting Message

# Write a program that prints "Hello, Python Learner!".

# Add Two Numbers

# Ask the user for two numbers using input(), add them, and print the result.

# Find the Square of a Number

# Take a number from the user as input and print its square (the number multiplied by itself).

# Check Even or Odd

# Get a number from the user, and print whether it is even or odd (Hint: use the modulus operator %).

# Simple Calculator

# Take two numbers and an operator (+, -, *, /) as input. Print the calculated result based on the operator.
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
if (y % 2 == 1):
    print("Odd number")
else:
    print("Even number")
operation = input("Enter your operation :")
match operation:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "/":
        print(x/y)
    case "*":
        print(int(x * y))
