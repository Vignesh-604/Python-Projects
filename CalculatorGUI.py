# Write a python GUI program to implement a  basic calculator app , with numeric buttons for input ,buttons for basic operations.
from tkinter import *
root = Tk()
root.title("Simple Calculator")
e1 = Entry(root, font="Arial", relief=SUNKEN, bd=5, state="readonly",justify="right")
l1 = Label(root, text="", font=("Arial",24))
l1.grid(column=4)
e1.grid(row=0, columnspan=4)


def delete():
    e1.configure(state="normal")
    e1.delete(0, END)
    l1.configure(text="")
    e1.configure(state="readonly")

def backs():
    e1.configure(state="normal")
    e1.delete(len(e1.get()) - 1, END)
    e1.configure(state="readonly")

def fun1(x):
    e1.configure(state="normal")
    e1.insert(len(e1.get()), x)
    e1.configure(state="readonly")

def eq():
    e = e1.get()
    ev = eval(e)
    l1.configure(text=str(ev))
    print(eval(e))
b1 = Button(root,text="1",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("1"))
b1.grid(row=1)
b2 = Button(root,text="2",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("2"))
b2.grid(row=1,column=1)
b3 = Button(root,text="3",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("3"))
b3.grid(row=1,column=2)
ba = Button(root,text="+",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("+"))
ba.grid(row=1,column=3)

b4 = Button(root,text="4",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("4"))
b4.grid(row=2)
b5 = Button(root,text="5",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("5"))
b5.grid(row=2,column=1)
b6 = Button(root,text="6",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("6"))
b6.grid(row=2,column=2)
bs = Button(root,text="-",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",padx=6,command=lambda: fun1("-"))
bs.grid(row=2,column=3)

b7 = Button(root,text="7",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("7"))
b7.grid(row=3)
b8 = Button(root,text="8",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("8"))
b8.grid(row=3,column=1)
b9 = Button(root,text="9",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("9"))
b9.grid(row=3,column=2)
bm = Button(root,text="*",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",padx=4,command=lambda: fun1("*"))
bm.grid(row=3,column=3)

bbl = Button(root,text="(",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",padx=6,command=lambda: fun1("("))
bbl.grid(row=4)
b0 = Button(root,text="0",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: fun1("0"))
b0.grid(row=4,column=1)
bbr = Button(root,text=")",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",padx=5,command=lambda: fun1(")"))
bbr.grid(row=4,column=2)
bd = Button(root,text="/",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",padx=7,command=lambda: fun1("/"))
bd.grid(row=4,column=3)

bdot = Button(root,text=".",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",padx=6,command=lambda: fun1("."))
bdot.grid(row=1,column=4)
b0 = Button(root,text="=",font=("Arial",30,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",command=lambda: eq())
b0.grid(row=2,column=4)
be = Button(root,text="DEL",font=("Arial",16,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",pady=20,command=backs)
be.grid(row=3,column=4)
bd = Button(root,text="CA",font=("Arial",16,"bold"),relief=RAISED,bd=5,bg="#02021E",fg="#00FF00",pady=20,padx=5,command=delete)
bd.grid(row=4,column=4)

root.mainloop()
