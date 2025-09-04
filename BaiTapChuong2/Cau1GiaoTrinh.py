'''
người a có số tiền x, gửi tk lãi 0.6%. gửi 18 tháng a có nhiêu tiền? 
6 tháng tiền lãi cộng vào gốc, a không rút tiền
Viết CT cho a nhập số tiền x vào tính tổng tiền sau 18 tháng.
'''
lai = 0.006
tien = int(input("Nhập số tiền X: "))
'''
lãi  6 tháng = tiền gốc * (lãi * 6)
-> hệ số tiền tăng sau mỗi 6 tháng: 1 + lãi * 6
'''
sotientang = 1 + lai * 6
#có 18 tháng -> 3 chu kì 6 tháng
tongtien = tien * (sotientang**3)
print("Tổng tiền sau 18 tháng: ", tongtien)
