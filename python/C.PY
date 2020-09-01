from tkinter import *

top=Tk()

class backcolor:
    def __init__(self,master):
        self.master=master
        master.geometry("300x300")
        self.button=Checkbutton(master,text="red",command=self.red).place(x=100,y=50)
        self.button=Checkbutton(master,text="yellow",command=self.yellow).place(x=100,y=100)
        self.button=Checkbutton(master,text="green",command=self.green).place(x=100,y=150)
        self.button=Checkbutton(master,text="blue",command=self.blue).place(x=100,y=200)
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
