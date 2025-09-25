
s = "  Python cơ bản  "

# strip(): Xóa khoảng trắng đầu và cuối chuỗi
print(s.strip()) 

# lower(): Chuyển chuỗi thành chữ thường
print(s.lower())  

# upper(): Chuyển chuỗi thành chữ hoa
print(s.upper())  

# replace(old, new): Thay thế chuỗi con
print(s.replace("cơ bản", "nâng cao"))  

# split(sep): Tách chuỗi thành danh sách
print(s.split())  

# join(list): Nối các phần tử thành chuỗi
lst = ['Python', 'cơ', 'bản']
print(" ".join(lst))  

# isupper(): Kiểm tra chuỗi có phải toàn chữ hoa không
print(s.isupper())

# islower(): Kiểm tra chuỗi có phải toàn chữ thường không
print(s.islower())

# isdigit(): Kiểm tra chuỗi có phải toàn số không
print(s.isdigit())  

# len(): Độ dài chuỗi
print(len(s))       

# isspace(): Kiểm tra chuỗi có phải toàn khoảng trắng không
print(s.isspace())  

