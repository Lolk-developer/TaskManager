from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from datetime import date

def windown1():  # Напоминания
    Win1 = Tk()
    Win1.title("Напоминания")
    Win1.geometry("600x710")
    Win1.resizable(False, False)

    def create_task():  # Create task
        task = Createtask.get()
        if task != "":
            Tasklist.insert(0, task)
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, введите напоминание.")


    def edit_win():
        global redact
        task = Tasklist.curselection()
        def update_task():
            Tasklist.delete(task)
            Tasklist.insert(task,Updtask.get())
            Win3.destroy()

        if task:
           Win3= Tk()
           Win3.title("Редактирование задачи")
           Win3.geometry("500x200")
           Updtask = ttk.Entry(Win3, width=65)
           Updtask.insert(0,Tasklist.get(task))
           Updtask.place(relx=0.1, rely=0.3)
           Updbtn = ttk.Button(Win3, text="Сохранить", command=update_task)
           Updbtn.place(relx=0.42, rely=0.6)
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, ввыберете упоминание!")

    
    def delete_task():
        task = Tasklist.curselection()
        if task:
            Tasklist.delete(task)
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, ввыберете упоминание!")

    def Archiv():
        global archiv
        Win2 = Tk()
        Win2.title("Архив")
        Win2.geometry("500x600")
        archiv = Listbox(Win2)
        archiv.place(relx=0, rely=0, relwidth=1, relheight=0.9)
        DelArch = ttk.Button(Win2, text="Удалить", command=delete_Archiv)
        DelArch.place(relx=0.420, rely=0.9)

    def delete_Archiv():
        global ark
        ark = archiv.curselection()
        if ark:
            archiv.delete(ark)
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, выберете упоминание!")

    def end_task():
        task = Tasklist.curselection()
        if task:
            Archiv()
            select_task = Tasklist.get(task)
            archiv.insert(END, select_task)
            Tasklist.delete(task)
            with open('archiv.TXT', 'a') as file:
                file.write(select_task + '\n')
        else:
            showerror("Ничего не выбрано", "Выберите что-то")

    Createtask = ttk.Entry(Win1)
    Createtask.place(rely=0, relx=0, relwidth=1)

    Createbtn1 = ttk.Button(Win1, text="Создать", command=create_task)
    Createbtn1.place(relx=0, rely=0.05)

    Editbtn1 = ttk.Button(Win1, text="Редактировать", command=edit_win)
    Editbtn1.place(relx=0.175, rely=0.05)

    Endbtn1 = ttk.Button(Win1, text="Завершить", command=end_task)
    Endbtn1.place(relx=0.42, rely=0.05)

    Delbtn = ttk.Button(Win1, text="Удалить", command=delete_task)
    Delbtn.place(relx=0.625, rely=0.05)

    Archivebtn = ttk.Button(Win1, text="Архив задач", command=Archiv)
    Archivebtn.place(relx=0.8, rely=0.05)

    Tasklist = Listbox(Win1)
    Tasklist.place(relx=0, rely=0.15, relwidth=1, relheight=0.9)


notes_list = []

def notion():
    Win2 = Tk()
    Win2.title("Заметки")
    Win2.geometry("600x710")
    Win2.resizable(False, False)

    def new_notes():
        Nnotes = Tk()
        Nnotes.title("Создание новой заметки")
        Nnotes.geometry("600x710")
        Nnotes.resizable(False, False)

        label1 = ttk.Label(Nnotes, text="Заголовок")
        label1.place(relx=0)

        title = ttk.Entry(Nnotes)
        title.place(relx=0, rely=0.04, relwidth=1)

        label2 = ttk.Label(Nnotes, text="Текст")
        label2.place(relx=0, rely=0.11)

        maintext = ttk.Entry(Nnotes)
        maintext.place(relx=0, rely=0.15, relwidth=1, relheight=0.75)

        def save_note():
            note_title = f"{title.get()} \n (дата создания:{date.today()})"
            note_text = maintext.get()

            if note_title:
                notes_list.append((note_title, note_text))
                NoteList.insert("end", note_title)

            Nnotes.destroy()

        save_btn = ttk.Button(Nnotes, text="Сохранить", command=save_note)
        save_btn.place(relx=0.4, rely=0.9)

    def read_note():
        selected_index = NoteList.curselection()
        if selected_index:
            selected_index = selected_index[0]
            note_title, note_text = notes_list[selected_index]

            ReadNote = Tk()
            ReadNote.title(f"{note_title}")
            ReadNote.geometry("600x710")
            ReadNote.resizable(False, False)

            label1 = ttk.Label(ReadNote, text=note_title, font=("Helvetica", 16))
            label1.pack(pady=10)

            label2 = ttk.Label(ReadNote, text=note_text, wraplength=500, justify="left")
            label2.pack(pady=10)

        else:
            showerror("Ошибка", "Выберите заметку для чтения")

    
    def delete_note():
        selected_index = NoteList.curselection()
        if selected_index:
            selected = selected_index[0]
            notes_list.pop(selected) #ведь удаляет по индексу
            NoteList.delete(selected_index)
        else:
            showerror("Ошибка", "Выберите заметку для удаления")

    def shortnotion():
        Shortwin = Tk()
        Shortwin.title("Быстрая заметка")
        Shortwin.geometry("200x200")
        Shortwin.resizable(False, False)

        shorttext = ttk.Entry(Shortwin)
        shorttext.place(relwidth=1, relheight=1)


    Createbtn = ttk.Button(Win2, text="Создать", command=new_notes)
    Createbtn.place(relx=0)

    Readbtn = ttk.Button(Win2, text="Читать", command=read_note)
    Readbtn.place(relx=0.42)

    Delbtn = ttk.Button(Win2, text="Удалить", command=delete_note)
    Delbtn.place(relx=0.845)

    NoteList = Listbox(Win2)
    NoteList.place(relx=0, rely=0.05, relwidth=1, relheight=0.85)

    Shortbtn = ttk.Button(Win2, text="+", command=shortnotion)
    Shortbtn.place(relx=0.92, rely=0.9, relwidth=0.08)


Mainwindow = Tk()
Mainwindow.title("Главное меню")
Mainwindow.geometry("600x710")
Mainwindow.resizable(False, False)

Text = ttk.Label(text="Tast Manager", font=("Helvetica", 16))
Text.place(relx=0.426, rely=0.35)

btn = ttk.Button(text="Напоминания", command=windown1)
btn.place(relx=0, y=550, width=600, height=50)

btn1 = ttk.Button(text="Заметки", command=notion)
btn1.place(relx=0, y=620, width=600, height=50)

Mainwindow.mainloop()
