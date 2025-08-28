d=int(input("Nhap chieu dai:"))
rong=int(input("Nhap chieu rong:"))
for i in range(d):
    if i==0 or i== d-1:
        print("*"*rong)
    else:
        print("*"+" "*(rong-2)+"*")