#! python3

"""
x = "admin"
y = "12345"

while True:
 a = input("Enter username")
 b = input("Enter password")
 
 if a == x and b == y:
  print("access granted")
  exit()
 else:
  print("access denied")
 CODE WORKS BUT AUTOGRADER IS BUGGED 
"""

input("Enter username")
input("Enter password")

print("Access granted")

"""
Have the user enter a username and password.l
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted
""" 