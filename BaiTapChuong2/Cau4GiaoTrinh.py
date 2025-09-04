#nhap vao 1 thang xuat ra thang do co bao nhieu ngay, neu la thang 2 thi co  nhuan hay khong 
thang = int(input("Vui lòng nhập 1 tháng: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8  or thang == 12:
    print("Tháng ",thang," có 31 ngày.")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print("Tháng ",thang," có 30 ngày.")
elif thang == 2: 
    kt = input("Có nhuần hay không?(Nhuần nhập 'n, không nhập 'k'): ")
    if kt == "n":
        print("Tháng ",thang, " có 29 ngày.")
    else: 
        print("Tháng ",thang, " có 28 ngày.")
else:
    print("Thông tin nhập sai!")