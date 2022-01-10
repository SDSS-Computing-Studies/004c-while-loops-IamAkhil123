#! python3


while a == "admin" and b == "12345":
 a = input("Enter password")
 b = input("Enter username")


if a == "admin" and b == "12345":
  print("Access granted")
else:
  print("Access denied")

"""
password = input("Enter password:")
Password = "12345"

while password == False:
    print("Access denied")
    if password == Password:
        print("Access granted")
"""

"""
Have the user enter a username and password.
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