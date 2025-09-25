def toi_uu_chuoi(s):
    # Xóa khoảng trắng đầu cuối, tách các từ, loại bỏ khoảng trắng dư
    words = s.strip().split()
    # Viết hoa chữ cái đầu mỗi từ, các chữ cái còn lại viết thường
    words = [w.capitalize() for w in words]
    # Ghép lại thành chuỗi với 1 khoảng trắng giữa các từ
    return ' '.join(words)

s = input("Nhập chuỗi: ")
print(toi_uu_chuoi(s))