print("Chuong trinh doc so thanh chu:")
n=int(input("Nhap vao so co 2 chu so:"))
if n < 99 and n > 0:
    tam = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
    if n == 0:
        doc= "không"

    elif n < 10:
        doc= tam[n]
    elif n >10 and n<20:
        donvi=n%10
        if donvi == 0:
            doc = "mười"
        elif donvi == 15: 
            doc = "mười lăm"
        else: 
            doc = "mười" + tam[donvi]
    else:
        chuc=n//10
        donvi=n%10
        doc = tam[chuc] + " mươi"
        if donvi == 1: 
            doc += " mốt"
        elif donvi == 5: 
            doc += " lăm"
        elif donvi != 0: 
            doc += " " + tam[donvi]
    print(f"Số đọc là: {doc}")

else:
    print("Sai yeu cau!")