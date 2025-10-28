from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("Enter New Password")
root.minsize(height=200,width=350)
root.resizable(height=True,width=True)

stringMacDinh="lenhuthao123"

def Sosanh():
    
    if stringOld.get()=="" or stringNew.get()=="" or stringAgain.get()=="":
        messagebox.showinfo('Thông báo','Vui long nhap đủ thông tin')
    elif stringOld.get()!=stringMacDinh:
        messagebox.showinfo('Thông báo','Mật khẩu cũ không đúng')
    elif stringOld.get()==stringMacDinh and stringNew.get()==stringMacDinh:
        messagebox.showinfo('Thông báo','Mật khẩu mới phải khác mật khẩu cũ')
    elif stringNew.get()!=stringAgain.get():
        messagebox.showinfo('Thông báo','Xác nhận mật khẩu mới không đúng')
    elif stringOld.get()=="" or stringNew.get()=="" or stringAgain.get()=="":
        messagebox.showinfo('Thông báo','Vui long nhap đủ thông tin')
    else:
        messagebox.showinfo('Thông báo','Đã thay đổi thành công')
        stringOld.set("")
        stringNew.set("")
        stringAgain.set("")
        

stringOld=StringVar()
stringNew=StringVar()
stringAgain=StringVar()

Label(root,text="Old Password:").grid(row=0,column=0)
Entry(root,width=30, textvariable=stringOld, show ="*").grid(row=0,column=1)
Label(root,text="New Password:").grid(row=1,column=0)
Entry(root,width=30,textvariable=stringNew,show ="*").grid(row=1,column=1)
Label(root,text="Enter New Password Again:").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringAgain,show ="*").grid(row=2,column=1)

frameButton=Frame(root)
Button(frameButton,text="OK",command=Sosanh).pack(side=LEFT)
Button(frameButton,text="Thoát",command=root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)
root.mainloop()