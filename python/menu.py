from tkinter import *

top=Tk()
                 
class menu:      
    def __init__(self,root):
        self.root=root
        root.geometry("700x600")
        root.title("GST da dhaba")
        root.configure(background="cyan")
        master=Frame(root).place(x=50,y=100,width=500,height=400)
        Label(master,text="MENU",font=("courier",'32'),bg="cyan").place(x=250,y=50)
        self.label1=Label(master,text="item").place(x=150,y=120)
        self.label2=Label(master,text="price").place(x=250,y=120)
        self.label3=Label(master,text="quantity").place(x=350,y=120)
        self.sa=IntVar()
        self.checksamosa=Checkbutton(master,text="Samosa",variable=self.sa,onvalue=1,offvalue=0).place(x=150,y=150)
        self.labelsa=Label(master,text="₹ 30").place(x=250,y=150)
        self.qusa=IntVar()
        self.entrysa=Entry(master,textvariable=self.qusa).place(x=350,y=150)
        self.ch=IntVar()
        self.checkchow=Checkbutton(master,text="chowmine",variable=self.ch,onvalue=1,offvalue=0).place(x=150,y=200)
        self.labelsa=Label(master,text="₹ 200").place(x=250,y=200)
        self.quchow=IntVar()
        self.entrysa=Entry(master,textvariable=self.quchow).place(x=350,y=200)
        self.man=IntVar()
        self.checkman=Checkbutton(master,text="manchurian",variable=self.man,onvalue=1,offvalue=0).place(x=150,y=250)
        self.labelsa=Label(master,text="₹ 300").place(x=250,y=250)
        self.quman=IntVar()
        self.entrysa=Entry(master,textvariable=self.quman).place(x=350,y=250)
        self.fr=IntVar()
        self.checksamosa=Checkbutton(master,text="fried rice",variable=self.fr,onvalue=1,offvalue=0).place(x=150,y=300)
        self.labelsa=Label(master,text="₹ 200").place(x=250,y=300)
        self.qufr=IntVar()
        self.entrysa=Entry(master,textvariable=self.qufr).place(x=350,y=300)
        self.button1=Button(master,text="calculate bill",command=self.bill).place(x=150,y=350)
        self.billt=IntVar()
        Entry(master,textvariable=self.billt).place(x=250,y=350)
        
        Label(master,text="jis jis ne khane ka bill nahi diya hai",font=("courier",'15','bold')).place(x=50,y=400)
        Label(master,text=" wo apne tashreef ke tokre laker ",font=("courier",'20','bold')).place(x=50,y=430)
        Label(master,text="  yaha se leker nikal jaye",font=("courier",'20','bold')).place(x=50,y=470)
        
    
    def bill(self):
        self.tot=0
        if(self.sa.get()==1):
           self.tot=self.qusa.get()*30+self.tot
        if(self.ch.get()==1):
            self.tot=self.quchow.get()*200 +self.tot 
        if(self.fr.get()==1):
            self.tot=self.tot + self.qufr.get()*200
        if(self.man.get()==1):
            self.tot=self.tot+self.quman.get()*300
        self.billt.set(self.tot)



my=menu(top)
top.mainloop()
