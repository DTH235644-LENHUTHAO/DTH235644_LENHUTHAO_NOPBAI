a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
ch = (input("Nhập toán tử (+, -, *, /): "))
if ch == "+":
    kq = a + b; 
    print(kq)
    n = 1
elif ch == "-":
    kq = a - b
    print(kq)
    n = 1
elif ch == "*":
    kq = a * b
    print(kq)
    n = 1
elif ch == "/":
    kq = a / b
    print(kq)
    n = 1
else: 
    print("Kí tự ",ch," không phải là một toán tử!")

