from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
#import os

def windown1(): #Напоминания
    Win1 = Tk()
    Win1.title("Напоминания")
    Win1.geometry("600x710")
    Win1.resizable(False, False)

    def create_task(): #Create task
        global tasks
        task = Createtask.get()
        if task != "":
            Tasklist.insert(0, task)
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, введите напоминание.")


    Createtask = ttk.Entry(Win1)
    Createtask.place(rely=0, relx=0, relwidth=1)

    Createbtn1 = ttk.Button(Win1, text="Создать", command=create_task)
    Createbtn1.place(relx=0, rely=0.05)

    Editbtn1 = ttk.Button(Win1, text="Редактировать")
    Editbtn1.place(relx=0.175, rely=0.05)

    Endbtn1 = ttk.Button(Win1, text="Завершить")
    Endbtn1.place(relx=0.42, rely=0.05)

    Delbtn = ttk.Button(Win1, text="Удалить")
    Delbtn.place(relx=0.625, rely=0.05)

    Archivebtn = ttk.Button(Win1, text="Архив задач")
    Archivebtn.place(relx=0.8, rely=0.05)

    Tasklist = Listbox(Win1)
    Tasklist.place(relx=0, rely=0.15, relwidth=1, relheight=0.9)

    #Backbtn = ttk.Button(Win1, text="<- back")
    #Backbtn.placepack(anchor=NW)



Mainwindow = Tk()
Mainwindow.title("Notes") #Титл
Mainwindow.geometry("600x710") #Разрешние
Mainwindow.resizable(False, False)

tasks = []

#windows

Text = ttk.Label(text="Tast Manager", font=("Helvetica", 16))
Text.place(relx=0.426, rely=0.35)

#Button

btn = ttk.Button(text="Напоминания", command = windown1)
btn.place(relx=0, y=550, width=600, height=50)

btn1 = ttk.Button(text="Заметки")
btn1.place(relx=0, y=620, width=600, height=50)

Mainwindow.mainloop()