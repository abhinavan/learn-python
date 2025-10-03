# Ask the user to enter a comma-separated list of numbers (e.g., 1,2,3,4,5) and a number of shifts.
# Move the items to the right by the shift amount. For example, [1,2,3,4,5] shifted right by 2 becomes [4,5,1,2,3].
''' 
Here are some steps—try to work them one at a time:
Parse the input: Turn "1,2,3,4,5" into a list of numbers: `` (using split and int() on each item)
Normalize the shifts: If shifts > length, use remainder: shifts = shifts % len(list)
Slice the list: In Python, you can use slicing to get parts of a list: list[start:end]. Can you figure out how to combine slices to "rotate" the list?
For example, grabbing the last shifts elements and putting them in front of the rest.
Print the rotated list: Output the new list.
'''

inputNumbers = input("Enter numbers comma-separated \n")
shift = int(input("Enter the shifts (right rotation) \t"))
inputList = list(map(int, inputNumbers.split(",")))
print(inputList)

if (shift > len(inputList)):
    shift = shift % len(inputList)

# Clarified: This rotates right by taking last 'shift' elements and moving them to front
rotated = inputList[-shift:] + inputList[:-shift]
print("Rotated list (right by", shift, "):", rotated)
