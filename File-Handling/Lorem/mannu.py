# !/bin/python3


# def reverseString(string):
#     string = list(string)
#     print(type(string))
#     print(string)
#     if (string == (string.reverse())):
#         print("This is palindrome")

#     else:
#         print("This word is not a palindrome")

#     return string


# test = reverseString("emmanuel")
# print(test)
# testOne = reverseString("mom")
# print(testOne)
import random

def generate_Password(self):
    
    print('''
    Password Generator
    ==================
    ''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

length = 9

print('\nhere are your passwords:')
password = ''
for c in range(0, length):
    password += random.choice(chars)
print(password)
pass

generate_Password(self)