#Nhap 3 so a b c tren mot dong, kt xem co tao thanh 3 canh tam giac hay khong 
a, b, c = map(float, input("Nhập 3 giá trị a, b, c: ").split())
if a + b > c and a + c > b and b + c > a: 
    print("Có thể tạo thành 1 tam giác.")
else: 
    print("Không thể tạo thành 1 tam giác.")