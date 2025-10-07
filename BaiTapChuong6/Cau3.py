from random import randrange

def TaoMaTran(m,n):
    D=[]
    for i in range(m):
        row =[]
        for j in range(n):
            row.append(randrange(1,100))
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element,end="\t")
        print()

def LayDong(r):
    R=D[r]
    return R

def XuatList1Chieu(R):
    for element in R:
        print(element,end="\t" )

def LayCot(c):
    C=[]
    for i in range(len(D)):
        C.append(D[i][c])
    return C

def MAX(D):
    max=D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j]>max:
                max=D[i][j]
    return max

print("Nhập số dòng của ma trận:")
m=int(input())
print("Nhập số cột của ma trận:")
n=int(input())
D=TaoMaTran(m,n)
print("Ma trận vừa tạo là:")
XuatMaTran(D)

print("Nhập dòng muốn xuat:")
r=int(input())
XuatList1Chieu(LayDong(r))
print("\nMoi nhap cot muon xuat:")
c=int(input())
XuatList1Chieu(LayCot(c))
max=MAX(D)
print("\nPhần tử lớn nhất trong ma trận là:",max)