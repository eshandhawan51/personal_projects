from tkinter import *
import time 
from time import sleep
top=Tk()
class traffic:
    def __init__(self,root):
        self.root=root
        self.root.geometry("150x500")
        self.root.title("traffic light")
        self.can=Canvas(self.root,bg="black",height='498',width='148')
        self.can.place(x=0,y=0)
        self.oval1=(self.can).create_oval(25,25,125,125,fill="red") 
        self.oval2=(self.can).create_oval(25,150,125,250,fill="orange")
        self.oval3=(self.can).create_oval(25,275,125,375,fill="green")
        self.u=1
        self.buttona=Button(self.root,text="AUTO",command=self.loop).place(x=15,y=400)
        self.buttonm=Button(self.root,text="mannual",command=self.mannualset).place(x=85,y=400)
        
    def mannualset(self):
        self.buttonr=Button(self.root,text="red",command=self.red).place(x=10,y=450)    
        self.buttony=Button(self.root,text="yellow",command=self.yellow).place(x=45,y=450)  
        self.buttong=Button(self.root,text="green",command=self.green).place(x=100,y=450)
        self.u=0
        self.root.update()  
    def red(self):
        (self.can).itemconfigure(self.oval1,fill="red")
        (self.can).itemconfigure(self.oval2,fill="black")
        (self.can).itemconfigure(self.oval3,fill="black")
        self.root.update()
          
    def yellow (self):
        (self.can).itemconfigure(self.oval1,fill="black")
        (self.can).itemconfigure(self.oval2,fill="orange")
        (self.can).itemconfigure(self.oval3,fill="black")
        self.root.update()
    def green(self):
        (self.can).itemconfigure(self.oval1,fill="black")
        (self.can).itemconfigure(self.oval2,fill="black")
        (self.can).itemconfigure(self.oval3,fill="green")
        self.root.update()
        
    def loop(self):
        if(self.u==0):
            (self.buttonr).destroy()
            (self.buttony).destroy()
            (self.buttong).destroy()


        self.u=1
        while(self.u==1):
            self.red()
            time.sleep(1)
            self.yellow()
            time.sleep(1)
            self.green()
            time.sleep(1)
        self.root.update()    

my=traffic(top)
#my.loop()
top.mainloop()                             
