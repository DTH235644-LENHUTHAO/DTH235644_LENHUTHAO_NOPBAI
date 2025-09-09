print("Chuong trinh dem so ngay trong thang:")
month=int(input("Moi nhap vao 1 thang:"))
if month in (1,3,5,7,8,10,12):
    print("Thang ",month," co 31 ngay")
elif month in (4,6,9,11):
    print("Thang ",month," co 30 ngay")
elif month == 2:
    year=int(input("Moi nhap vao mot nam :"))
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Thang ",month," co 29 ngay")
    else:
        print("Thang ",month," co 28 ngay")
else:
    print("Thang ",month," khong hop le!")