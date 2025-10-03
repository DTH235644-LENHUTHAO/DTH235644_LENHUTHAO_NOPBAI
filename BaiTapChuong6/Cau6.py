from random import randrange
from random import sample

n = int(input("Nhập số phần tử của list: "))

lst = sample(range(1, 100), n)
print("List ngẫu nhiên không trùng nhau là:")
print(lst)