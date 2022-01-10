#! python3
import time

x = "admin"
y = "12345"

while True:
 username = input("Enter username")
 password = input("Enter password")
 
 if username == x and password == y:
  print("access granted")
  exit()
 else:
  print("access denied")

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