#! python3

while True:
    number = float(input("enter a number"))
    x = int(number)
    if x == 0:
        break

    y = x % 2

    if y > 0:
        print("That is not an even integer")
    else:
        print("That is an even integer")
        exit()

"""  
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)
inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer
"""





