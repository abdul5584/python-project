import tkinter as tk
window=tk.Tk()
window.geometry('400x400')
window.title('calc')
lblnum1=tk.Label(window,text='NUM1')
lblnum1.place(x=100,y=100)
a=tk.StringVar()
b=tk.StringVar()
c=tk.StringVar()
txtnum1=tk.Entry(window,textvariable=a)
txtnum1.place(x=200,y=100)
lblnum2=tk.Label(window,text='NUM2')
lblnum2.place(x=100,y=150)
txtnum2=tk.Entry(window,textvariable=b)
txtnum2.place(x=200,y=150)
lblnum3=tk.Label(window,text='RESULT')
lblnum3.place(x=100,y=200)
txtnum3=tk.Entry(window,state=tk.DISABLED,textvariable=c)
txtnum3.place(x=200,y=200)
def add():
   m=int(a.get())+int(b.get())
   c.set(str(m))
def clr():
    a.set('')
    b.set('')
    c.set('')
btnadd=tk.Button(window,text='ADD',command=add)
btnadd.place(x=100,y=250)
btnclr=tk.Button(window,text='CANCEL',command=clr)
btnclr.place(x=200,y=250)
window.mainloop()