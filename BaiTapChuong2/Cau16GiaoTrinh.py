day = int(input("Nhập day: "))
month = int(input("Nhập month: "))
year = int(input("Nhập year: "))
#kiểm tra tháng
if month < 1 or month > 12:
    print("Tháng không hợp lệ!")
else: 
    #số ngày
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else: #tháng 2
        #kt năm nhuần
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            max_day = 29
        else: 
            max_day = 28
    #Ngày
    if day < 1 or day > max_day: 
        print("Ngày không hợp lệ!")
    else: 
        print(f"Kết quả:{day}/{month}/{year}")