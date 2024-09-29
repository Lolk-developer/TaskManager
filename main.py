import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
#import os

def windown1(): #Напоминания
    Win1 = Tk()
    Win1.title("Напоминания")
    Win1.geometry("600x710")
    Win1.resizable(False, False)
    archiv_task=None #Храним наш недо-архив

    def create_task(): #Create task
        global tasks
        task = Createtask.get()
        if task != "":
            Tasklist.insert(0, task)
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, введите напоминание.")
    def delete_task():
       global tasks #а зачем?
       task=Tasklist.curselection()
       if task:
         Tasklist.delete(task)
       else:
          showerror(title="Пустое поле.", message="Пожалуйста, ввыберете упоминание!")

    def end_task():
        task = Tasklist.curselection()
        if task:
            select_task=Tasklist.get(task)
            archiv_task.insert(END, select_task)
            Tasklist.delete(task)
        else:
            showerror("Ничего не выбрано", "Выберите что-то")

    Createtask = ttk.Entry(Win1)
    Createtask.place(rely=0, relx=0, relwidth=1)

    Createbtn1 = ttk.Button(Win1, text="Создать", command=create_task)
    Createbtn1.place(relx=0, rely=0.05)

    Editbtn1 = ttk.Button(Win1, text="Редактировать")
    Editbtn1.place(relx=0.175, rely=0.05)

    Endbtn1 = ttk.Button(Win1, text="Завершить", command=end_task)
    Endbtn1.place(relx=0.4, rely=0.05)

    Delbtn = ttk.Button(Win1, text="Удалить", command=delete_task)
    Delbtn.place(relx=0.625, rely=0.05)

    Archivebtn = ttk.Button(Win1, text="Архив задач",)
    Archivebtn.place(relx=0.8, rely=0.05)

    Tasklist = Listbox(Win1)
    Tasklist.place(relx=0.1, rely=0.3)

    archiv_task = Listbox(Win1)
    archiv_task.place(relx=0.5, rely=0.3)



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
