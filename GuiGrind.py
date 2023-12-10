from tkinter import * #*=importall
from tkinter import ttk


GUI = Tk()
GUI.title('Flashcard by Victah')
GUI.geometry('500x500')

L1 = ttk.Label(GUI,text='Knowledge Cat')
L1.pack()

E1 = ttk.Entry(GUI, font=('Angsana New',24))
E1.pack()

L2 = ttk.Label(GUI,text='Description', font=('Angsana New', 26))
L2.pack()

T1 = Text(GUI, font=('Angsana New', 26) , height= 8 , width = 18 )
T1.pack()

GUI.mainloop()  #mainloop = ทำให้โปรแรกมทำงานได้ตลอดโดยไม่ปิด