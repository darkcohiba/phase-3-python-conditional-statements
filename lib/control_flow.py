#!/usr/bin/env python3

# def admin_login(username, password):
#     if username == 'admin' or username == 'ADMIN':
#         if password == '12345':
#             return 'Access granted'
#         else:
#             return 'Access denied'
#     else:
#         return 'Access denied'

def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'
    

def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif temperature > 65:
        return "It's perfect out there!"
    elif temperature > 40:
        return "It's a little chilly out there!"
    else:
        return "It's brisk out there!"
    

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    return (num1 + operation + num2)
    


