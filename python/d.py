from tkinter import *

top=Tk()

class sum:
    def __init__(self,master):
        self.master=master
        master.geometry("300x300")
        image1=PhotoImage(file="C:\\Users\\eshan\\Downloads\\th1.png")
        self.back=Label(master,image=image1).place(x=1,y=1,relwidth=1,relheight=1)
        master.title("sum of 2 numbers ")
        self.label=Label(master,text="enter two numbers").place(x=100,y=30)
        self.no1=IntVar()
        self.no2=IntVar()
        Entry(master,text="number 1",textvariable=self.no1).place(x=50,y=90)
        Entry(master,text="number 2",textvariable=self.no2).place(x=150,y=90)
        self.button=Button(master,text="sum",command=self.sum1).place(x=100,y=150)
        self.res=IntVar()
        Entry(master,text="result",textvariable=self.res).place(x=100,y=200)
    def sum1(self):
        a=self.no1.get()
        b=self.no2.get()
        c=a+b
        self.res.set(c)        

my=sum(top)


top.mainloop()
