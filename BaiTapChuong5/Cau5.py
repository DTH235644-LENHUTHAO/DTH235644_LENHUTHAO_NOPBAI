s = input("Nhập chuỗi: ")

in_hoa = 0
in_thuong = 0
chu_so = 0
ky_tu_dac_biet = 0
khoang_trang = 0
nguyen_am = 0
phu_am = 0

nguyen_am_set = set("aeiouyAEIOUY")

for ch in s:
    if ch.isupper():
        in_hoa += 1
    if ch.islower():
        in_thuong += 1
    if ch.isdigit():
        chu_so += 1
    if ch.isspace():
        khoang_trang += 1
    if not ch.isalnum() and not ch.isspace():
        ky_tu_dac_biet += 1
    if ch.isalpha():
        if ch in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

print("Chữ IN HOA:", in_hoa)
print("Chữ in thường:", in_thuong)
print("Chữ số:", chu_so)
print("Ký tự đặc biệt:", ky_tu_dac_biet)
print("Khoảng trắng:", khoang_trang)
print("Nguyên âm:", nguyen_am)
print("Phụ âm:", phu_am)