def CheckDoiXung(s):
    flag=True
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            flag=False
            break
    return flag
def main():
    print("Nhap 1 chuoi:")
    s=input()
    if(CheckDoiXung(s)):
        print("Chuoi doi xung")
    else:
        print("Chuoi khong doi xung")
while True:
    main()
    print("Tiep tuc nhap hay khong (c/k):")
    s=input()
    if(s=='k'):
        break
print("Cam on da dung!")