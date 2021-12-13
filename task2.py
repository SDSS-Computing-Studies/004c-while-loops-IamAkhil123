#! python3
input().strip()
print("enter the username")
x = input()
print("enter the password")
b = input()

if str(x) == "admin" and str(b) == "12345":
    print ("Access granted")
else:
     print ("Access denied")
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