#Ve hinh
n=4
for i in range(n):
    if i==0:
        print("*"*4)
    elif i==1 or i==2:
        print("*"+" "*2+"*")
    elif i==3:
        print("*"*4)

n=4
for i in range(n):
    if i==0:
        print(" "*3+"*")
    elif i==1:
        print(" "*2+"*"*2)
    elif i==2:
        print(" "+"*"*3)
    elif i==3:
        print("*"*4)
