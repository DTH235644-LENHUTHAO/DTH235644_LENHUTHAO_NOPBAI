from tkinter import *

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def Giai():
    a=float(stringHSA.get())
    b=float(stringHSB.get())
    if a==0 and b==0:
        stringKQ.set("Vô số nghiệm")
    elif a==0 and b!=0:
        stringKQ.set("Vô nghiệm")
    else:
        stringKQ.set("x="+str(-b/a))

root =Tk()
root.title("PTB1")

stringHSA=StringVar()
stringHSB=StringVar()
stringKQ=StringVar()

root.minsize(height=150,width=250)
root.resizable(height=True,width=True)

Label(root,text="Phương trình bậc 1",fg="blue",font=("tohama",16)).grid(row=0,columnspan=2)

Label(root,text="Hệ số a:").grid(row=1,column=0)
Entry(root,width=30,textvariable=stringHSA).grid(row=1,column=1)

Label(root,text="Hệ số b:").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringHSB).grid(row=2,column=1)

frameButton=Frame()
Button(frameButton,text="Giải",command=Giai).pack(side=LEFT)
Button(frameButton,text="Tiếp",command=tiepAction).pack(side=LEFT)
Button(frameButton,text="Thoát",command=root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)
Label(root,text="Kết quả:").grid(row=4,column=0)
Entry(root,width=30,textvariable=stringKQ).grid(row=4,column=1)
root.mainloop()