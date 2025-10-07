n = int(input("Nhập số lượng phần tử: "))
M = []

for i in range(n):
    x = float(input(f"Nhập số thực M[{i}]: "))
    M.append(x)

M.sort(reverse=True)

print("Dãy số sau khi sắp xếp giảm dần là:")
print(M)

M.sort()

print("Dãy số sau khi sắp xếp tăng dần là:")
print(M)