#! python3


print("enter a number")
x = input()
if (float(x) % 2) == 0:
 print("That is an even integer")
else:
 while (float(x) % 2) == 0:
  print("enter a number")
  input()


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





