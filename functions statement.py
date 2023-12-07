#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      USER
#
# Created:     09-10-2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sayhello(username):
    greet="hello"
    print(greet + " " + username)

users = ['Ram','mahesh','vasudha','uma']
for name in users:
    sayhello(name)