from tkinter import *

top=Tk()

class backcolor:
    def __init__(self,master):
        self.master=master
        master.geometry("300x300")
        master.title("changing the background color")
        q=IntVar()
        self.button=Radiobutton(master,text="red",command=self.red,variable=q,value=1).place(x=100,y=50)
        self.button=Radiobutton(master,text="yellow",command=self.yellow,variable=q,value=2).place(x=100,y=100)
        self.button=Radiobutton(master,text="green",command=self.green,variable=q,value=3).place(x=100,y=150)
        self.button=Radiobutton(master,text="blue",command=self.blue,variable=q,value=4).place(x=100,y=200)
    def red(self):
        self.master.config(background="red")
    def yellow(self):
        self.master.config(background="yellow")
    def green(self):
        self.master.config(background="green")
    def blue(self):
        self.master.config(background="blue")    
my=backcolor(top)
top.mainloop()        