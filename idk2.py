from tkinter import *
from tkinter import ttk
from gtts import gTTS
import os
import googletrans
from googletrans import Translator

from PyPDF2 import PdfReader

reader = PdfReader("marks.pdf") #Add your PDF file name here

num_pages=(len(reader.pages))   

s = ""

for i in range(num_pages):
    page = reader.pages[i]
    s+=(page.extract_text())
# print(s)


root=Tk()
root.title("Language Translator")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background="black")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text
    language = 'en'
    tts = gTTS(text= trans_text, lang=language)
    tts.save("spoken_text.mp3")
    os.system("spoken_text.mp3")
    
    text2.delete(1.0,END)
    text2.insert(END,trans_text)
    
#icon

language= googletrans.LANGUAGES
languageV= list(language.values())
lang1= language.keys()

combo1=ttk.Combobox(root,values=languageV, font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE) 
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1= Text(f,font="Robote 20",bg="white", relief=GROOVE,wrap= WORD)
text1.place(x=0,y=0,width=430,height=200)
text1.insert(INSERT,s)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


combo2=ttk.Combobox(root,values=languageV,font="Roboto 14", state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)


f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2= Text(f1,font="Robote 20",bg="white", relief=GROOVE,wrap= WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button

translate=Button(root,text="Translate",font="Roboto 15 bold italic",activebackground="purple",cursor="hand2",bd=5,bg='red',fg="white",command=translate_now)
translate.place(x=480,y=200)

label_change()

root.mainloop()