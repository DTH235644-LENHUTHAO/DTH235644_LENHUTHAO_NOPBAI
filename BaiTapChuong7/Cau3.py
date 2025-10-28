from tkinter import *

def Cong():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(a+b)

def Tru():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(a-b)

def Nhan():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(a*b)

def Chia():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(a/b)

root = Tk()
root.title("PhepTinh")
stringA=StringVar()
stringB=StringVar()
stringKQ=StringVar()

root.minsize(height=150,width=200)
Label(root,text="Cộng Trừ Nhân Chia",fg=("blue"),font=("tohama",16)).grid(row=0,columnspan=3)
frameButton=Frame(root)
Button(frameButton,text="Cộng",command=Cong).pack(side=TOP,fill=X)
Button(frameButton,text="Trừ",command=Tru).pack(side=TOP,fill=X)
Button(frameButton,text="Nhân",command=Nhan).pack(side=TOP,fill=X)
Button(frameButton,text="Chia",command=Chia).pack(side=TOP,fill=X)
frameButton.grid(row=1,column=0,rowspan=4)

Label(root,text="Số a").grid(row=1,column=1)
Entry(root,width=15,textvariable=stringA).grid(row=1,column=2)
Label(root,text="Số b").grid(row=1,column=1)
Entry(root,width=15,textvariable=stringB).grid(row=2,column=2)
Label(root,text="Kết quả").grid(row=1,column=1)
Entry(root,width=15,textvariable=stringKQ).grid(row=3,column=2)

Button(root,text="Thoát",command=root.quit).grid(row=4,column=2)

root.mainloop()