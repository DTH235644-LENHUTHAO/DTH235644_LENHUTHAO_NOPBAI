import math
thu = ["thứ hai", "thứ ba", "thứ tư", "thứ năm", "thứ sáu", "thứ bảy", "chủ nhật"]
ngayden = "thứ tư"
ngayden = thu.index(ngayden) #hàm index tìm vị trí của phần tử thứ tư trong list thu (vị trí = 2)
#số ngày ở lại
ngay = 137

ketqua = (ngayden + (ngay % 7)) % 7
#ngay%7 vì 1 tuần có 7 ngày nên chu kì tuần sẽ lặp lại sau mỗi 7 ngày, chia dư -> phần nguyên sẽ là ngày 
#bắt đầu sau chu kì, còn phần dư sẽ là số ngày kế tiếp còn lại để biết được ngày vê
#ngayden + (...) cộng số dư vào vị trí của ngày bắt đầu, %7 một lần nữa để tránh lớn hơn list.
print(f"Sau {ngay} ngày kể từ {ngayden} là {thu[ketqua]}")
