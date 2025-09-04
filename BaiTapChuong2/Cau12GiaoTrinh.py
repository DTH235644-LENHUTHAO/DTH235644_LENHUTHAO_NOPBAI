n = int(input("Nhập số nguyên dương :"))
if n==0:
    print("Số nhị phân của",n,"là: 0")
else:
    nhiphan = ""
    x = n
    while x > 0:
        nhiphan = str(x % 2) + nhiphan
        x //= 2
    print("Số nhị phân của",n,"là:",nhiphan)