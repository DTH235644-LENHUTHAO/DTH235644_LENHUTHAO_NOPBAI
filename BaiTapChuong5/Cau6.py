def NegativeNumberInStrings(s):
    i = 0
    while i < len(s):
        if s[i] == '-' and i + 1 < len(s) and s[i+1].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            print(s[i:j])
            i = j
        else:
            i += 1
s = input("Nhap chuoi muon kiem tra: ")
NegativeNumberInStrings(s)