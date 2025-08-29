n  = 8
width = 11
for i in range(n):
    if i == 0:
        print(("*"*1).center(width))
    elif i == n - 7 or i == n - 5:
        print(("*"*3).center(width))
    elif i == n - 6:
        print(("*"*7).center(width))
    elif i == n - 4:
        print(("*"*5).center(width))
    elif i == n - 3:
        print(("*"*11).center(width))
    elif i == n - 2 or i == n - 1:
        print(("*" + " " + "*").center(width))