import math
print("Chuong trinh giai phuong trinh bac 2:")
a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
c=float(input("Nhap c:"))
if a==0:
    if b==0 and c==0:
        print("Vo so nghiem")
    elif b==0 and c!=0:
        print("Vo nghiem")
    else:
        x=-c/b
        print("Nghiem x=",x)
else:
    delta = b**2-4*a*c
    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        x=-b/(2*a)
        print("Nghiem kep x1=x2=",x)
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("x1=",x1)
        print("x2=",x2)