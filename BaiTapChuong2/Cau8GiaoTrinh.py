#nhap n (1<n<9) va in ra bang cuu chuong n
n = int(input("Nhập một số n  (1<n<9):  "))
if 1<n<9: 
    print(f"Bảng cửu chương {n}: ")
    for i in range(1,11): #từ 1 đến 10
        print(f"{n} x {i}  = {n*i}")
else: 
    print("Số n phải trong khoảng từ 1->9!")