from tkinter import *

top=Tk()

class menu:
    def __init__(self,master):
        self.master=master
        master.geometry("600x500")
        master.title("GST da dhaba")
        self.label1=Label(master,text="item").place(x=200,y=120)
        self.label2=Label(master,text="price").place(x=300,y=120)
        self.label3=Label(master,text="quantity").place(x=400,y=120)
        self.sa=IntVar()
        self.checksamosa=Checkbutton(master,text="Samosa",variable=self.sa,onvalue=1,offvalue=0).place(x=200,y=150)
        self.labelsa=Label(master,text="₹ 30").place(x=300,y=150)
        self.qusa=IntVar()
        self.entrysa=Entry(master,textvariable=self.qusa).place(x=400,y=150)

my=menu(top)
top.mainloop()
