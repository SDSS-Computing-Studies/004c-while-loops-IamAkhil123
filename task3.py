#! python3

from asyncio import staggered
from distutils.command.sdist import sdist
from readline import set_completion_display_matches_hook


x = input("enter a number")
print("That is not an even integer")
x = input("enter a number")
print("That is an even integer")
if x % 2 == 0:
  print("That is an even integer")
else:
  x = int(input("enter a number"))
  x = input("That is not an even integer")
  
  
print("Enter a number")

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





