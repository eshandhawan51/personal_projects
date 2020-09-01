#text to speech hello
import win32com.client as opt
#import pyaudio
import speech_recognition as sr
from tkinter import *

top=Tk()
class capabilities:
    def __init__(self,root):
        self.root=root
        self.root.geometry("300x350")
        
        
    def welcome (self):
        self.labelwelcome=Label(self.root,text="text  speech converter",font=("courier",'12','bold')).place(x=10,y=10)
        self.wel("welcome to text  speech converter ")
        self.root.update
    def texinpu(self):
        self.inputext=StringVar()
        self.inputext.set("hello, i am your text to speech converter ,type here what you want to convert to speech and then press the convert button")
        self.enter=Text(self.root,font=("courier",10))
        self.enter.place(x=10,y=50,width=250,height=200)
        self.e=self.enter.get("1.0","end")
        self.button=Button(self.root,text="convert",command=self.loop).place(x=50,y=275)
        self.button1=Button(self.root,text="speech to text",command=self.stt).place(x=150,y=275)
        
    def loop(self):
        self.ex=(self.enter).get("1.0","end")
        self.teller.voice(self.ex)


    def stt(self):
        self.con=listen()
        self.textres=self.con.listen() 
        self.enter.insert(INSERT,self.textres)
        self.root.update      
    def wel(self,u):
        self.user=u
        
        self.teller=speak()
        self.teller.voice(self.user)


class speak:
    def __init__(self):
        self.speaker=opt.Dispatch("SAPI.Spvoice")
    def voice(self,t):
        self.t=t
        (self.speaker).speak(t)
    
class listen:
    def __init__(self):
        self.r=sr.Recognizer()
    def listen (self):
        with sr.Microphone() as source:
            audio=self.r.record(source,duration=5)
            try:
                textout=self.r.recognize_google(audio,language="en_US")
                return(textout)
            except:
                return("retry")



my=capabilities(top)
my.welcome()
my.texinpu()
top.mainloop()
