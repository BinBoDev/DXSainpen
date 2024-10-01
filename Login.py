from tkinter import *
def login():
    pass
wdLogin = Tk()
wdLogin.title("Đăng nhập")
#Logo Mitsubishi
icon = PhotoImage(file='mitsubishi.png')
wdLogin.iconphoto(True,icon)
wdLogin.geometry("300x150")
wdLogin.resizable(False,False)
label1 = Label(wdLogin,text="User name").grid(row = 0,column = 0,padx = 10)
entry1 = Entry(wdLogin,width=30).grid(row =0,column = 1,pady = 10)
label2 =Label(wdLogin,text="Pass word").grid(row = 1,column = 0,padx=10)
entry2 = Entry(wdLogin,width=30,show="*").grid(row =1,column = 1,pady=10)
button1 = Button(wdLogin,text="Đăng nhập",command=login).grid(row = 2,column = 1,sticky = "W")
button2 = Button(wdLogin,text="Thoát",command=wdLogin.quit).grid(row = 2,column = 1,sticky = "E")

wdLogin.mainloop()