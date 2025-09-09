print("Chuong trinh tinh toan:")
a=int(input("Nhap vao so a:"))
b=int(input("Nhap vao so b:"))
pheptoan=input("Nhap vao phep toan +,-,*,/ :")

if pheptoan == "+":
    print("Ket qua a + b = ",a+b)
elif pheptoan == "-":
    print("Ket qua a - b = ",a-b)
elif pheptoan == "*":
    print("Ket qua a * b = ",a*b)
elif pheptoan == "/":
    print("Ket qua a / b = ",a/b)
else:
    print("Nhap sai phep toan!")