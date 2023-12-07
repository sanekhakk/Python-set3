
def addavg(x,y):
    s=x+y
    avg=s/2
    return s, avg

def sub(x,y):
    d=x-y
    return d

def mul(x,y):
    p=x*y
    return p

x=int(input("x: "))
y=int(input("y: "))

sum, average=addavg(x,y)
subtraction=sub(x,y)
multiplication=mul(x,y)

print("sum,average:",(sum,average))
print("subtraction:",subtraction)
print("multiplication:",multiplication)
