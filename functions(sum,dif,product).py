#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      USER
#
# Created:     04-10-2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def add(x,y):
    s=x+y
    print("sum:",s)

def sub(x,y):
    d=x-y
    print("difference:",d)

def mul(x,y):
    p=x*y
    print("product:",p)

x=int(input("x: "))
y=int(input("y: "))

add(x,y)
sub(x,y)
mul(x,y)
