from tkinter import * #*=importall
from tkinter import ttk
import csv
import os

path = os.getcwd()

notebutton = os.path.join(path,'notebutton.png')

print('PATH:',path)


def writecsv(data):
  # data = ['best',15,600]
  csvfile = os.path.join(path,'knowledge.csv')
  with open('knowledge.csv','a',newline='',encoding='utf-8') as file:
    fw = csv.writer(file)
    fw.writerow(data)


GUI = Tk()
GUI.title('Flashcard by Victah')
GUI.geometry('500x500')
GUI.iconbitmap(notebutton)

F1 = Frame(GUI)
F1.place(x=20,y=50)

L1 = ttk.Label(GUI,text='Knowledge Cat')
L1.pack()

V_title  = StringVar()

E1 = ttk.Entry(F1,textvariable=V_title, font=('Angsana New',24))
E1.pack()

L2 = ttk.Label(F1,text='Description', font=('Angsana New', 26))
L2.pack()

T1 = Text(F1, font=('Angsana New', 26) , height= 5 , width = 18 )
T1.pack()

def save():
  title = V_title.get()
  textbox = T1.get(1.0,"end-1c")
  print(title)
  print(textbox)
  print('-------')
  data = [title,textbox]
  writecsv(data)
  V_title.set('')  #clear data after save
  T1.delete('1.0',END) #Clear text box



B1 = ttk.Button(F1, text = 'save',command=save)
B1.pack(pady=10, ipadx=30, ipady=30)

#### Button Flash card ########

def readcsv():
    with open('knowledge.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data


knowledgelist = readcsv()
print(knowledgelist)

countindex = 0
GUI2 = None


def Flashcard():
    global GUI2
    GUI2 = Toplevel()
    GUI2.title('Study')
    GUI2.geometry('500x400')

    vtext_title = StringVar()
    vtext_detail = StringVar()
    tilte = ttk.Label(GUI2, textvariable=vtext_title, font=('Angsana New', 24))
    tilte.pack()
    vtext_title.set(knowledgelist[countindex][0])

    detail = ttk.Label(GUI2, textvariable=vtext_detail, font=('Angsana New', 18))
    detail.pack()
    vtext_detail.set(knowledgelist[countindex][1].replace('\r', ''))

    def Prev():
        global countindex
        if countindex == 0:
            countindex = countindex
        else:
            countindex = countindex - 1

        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1].replace('\r', ''))

    def Next():
        global countindex
        if countindex == (len(knowledgelist) - 1):
            countindex = len(knowledgelist) - 1
        else:
            countindex = countindex + 1

        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1].replace('\r', ''))

    Bprev = ttk.Button(GUI2, text='<', command=Prev)
    Bprev.place(x=150, y=350)
    Bnext = ttk.Button(GUI2, text='>', command=Next)
    Bnext.place(x=230, y=350)
  



notebutton = os.path.join(path,'notebutton.png')
notebutton = PhotoImage(file=notebutton)

BFlashcard = ttk.Button(GUI, image=notebutton, command=Flashcard)
BFlashcard.place(x=420,y=20)


GUI.mainloop()  #mainloop = ทำให้โปรแรกมทำงานได้ตลอดโดยไม่ปิด