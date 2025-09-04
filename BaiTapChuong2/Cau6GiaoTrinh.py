#viet pt giai pt bac hai ax^2 + bx + c = 0
import math
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
print("PT bậc 2: ",a,"x^2 + ",b,"x + ",c," = 0")
if a==0: 
    if b==0: 
        if c==0:
            print("PT VSN")
        else:
            print("PT VN")
    else:
        x = float(-c/b)
        print("PT có 1 nghiệm x = ",x)
else:
    delta  = float(b**2 - 4*(a*c))
    if delta > 0:
        x1 = float((-b + math.sqrt(delta))/2*a)
        x2 = float((-b - math.sqrt(delta))/2*a)
        print("PT có 2 nghiệm, x1 = ",x1,"; x2 = ",x2)
    elif delta == 0:
        x = float(-b/2*a)
        print("PT có nghiệm kép x1 = x2 = ",x)
    else:
        print("Delta < 0 => PT VN") 
