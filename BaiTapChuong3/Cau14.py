a=0
tam=0
while a<100:
    b=0
    while b<40:
        if(a+b)%2==0:
            print('*', end='')
            tam+=1
        b+=1
    print()
    a+=1
print("Co ",tam," dau * duoc in")