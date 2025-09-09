while True:
    n=int(input("Nhap 1 so nguyen duong:"))
    dem =0
    for i in range(1,n+1):
        if n%i==0:
            dem=dem+1
    if dem==2:
        print(n," la so nguyen to")
    else:
        print(n," khong phai la so nguyen to")
    tiep=input("Kiem tra tiep hay khong (c/k):")
    if tiep == "k":
        break
print("BYE!")