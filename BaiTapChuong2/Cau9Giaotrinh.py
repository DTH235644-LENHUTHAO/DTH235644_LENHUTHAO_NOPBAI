while True:
    n = int(input("Nhập một số dương:"))
    if n>0:
        break
    print("Nhập sai, mời nhập lại! ")
s=0
s1=0
s2=0
s3=0
s4=0

for i in range(1,n+1):
    s = s + i
    s1 += 2*i-1
    s2 += 2*i
    s3 += i**2
    s4 += 1/i

print("Kết quả:")
print("S =",s)
print("S1 =",s1)
print("S2 =",s2)
print("S3 =",s3)
print("S4 =",s4)