# Task 7

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import string
from random import *

if __name__ == '__main__':

    restart = True

    while restart:

        option = str(input('\nSelect password type: weak or strong? \n'))

        if option == 'weak':
            characters = string.ascii_letters
        else:
            characters = string.ascii_letters + string.punctuation + string.digits

        password = "".join(choice(characters) for x in range(8))
        print('New generated password is : ' + password)
        restart_ip = str(input('\nDo you want a new password: yes or no? \n'))

        if restart_ip == 'no':
            restart = False
