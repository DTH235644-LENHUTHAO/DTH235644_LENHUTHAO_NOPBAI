n = int(input("Nhap so phan tu của list:"))
lst=[]

for i in range(n):
    while True:
        x=int(input(f"Nhap phan tu thu {i+1}:"))
        if i==0 or x>lst[i-1]:
            lst.append(x)
            break
        else:
            print("Nhap lai")
print("Danh sach vua nhap la:")
print(lst)