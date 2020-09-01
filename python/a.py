from tkinter import *

top=Tk()

class sum:
    def __init__(self,master):
        self.master=master
        master.geometry("300x300")
       # img = PhotoImage(Image.open("C:\\Users\\eshan\\Downloads\\th1.png"))

        img=PhotoImage(file="ll.png")
        self.l1=Label(self.master,image=img)
        self.l1.place(x=0,y=0,relwidth=1,relheight=1)
          

#my=sum(top)

img=PhotoImage(file="ll.png")
l1=Label(top,image=img)
l1.place(x=0,y=0,relwidth=1,relheight=1)
top.mainloop()