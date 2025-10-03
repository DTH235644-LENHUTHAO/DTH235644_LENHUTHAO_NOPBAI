from random import randrange
print("Nhap so phan tu cua list:")
n=int(input())
lst=[0]*n
for i in range(n):
    lst[i]=randrange(1,100)
print("List ngau nhien la:")
print(lst)
print("Nhap so muon chen vao danh sach:")
value=int(input())
lst.append(value)
print("Danh sach sau khi chen la:")
print(lst)
print("Moi nhap so muon xoa trong danh sach:")
x=int(input())
while lst.count(x)>0:
    lst.remove(x)
print("Danh sach sau khi xoa la:")
print(lst)

def checkDoiXung(lst):
    for i in range(len(lst)):
        if(lst[i]!=lst[len(lst)-i-1]):
            return False
    return True

k=checkDoiXung(lst)
if k==True:
    print("List doi xung")
else:
    print("List khong doi xung")