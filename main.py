from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning

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
        archiv.pack()
        DelArch = ttk.Button(Win2, text="Удалить", command=delete_Archiv)
        DelArch.place(relx=0.420, rely=0.300)

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

    Editbtn1 = ttk.Button(Win1, text="Редактировать")
    Editbtn1.place(relx=0.175, rely=0.05)

    Endbtn1 = ttk.Button(Win1, text="Завершить", command=end_task)
    Endbtn1.place(relx=0.42, rely=0.05)

    Delbtn = ttk.Button(Win1, text="Удалить", command=delete_task)
    Delbtn.place(relx=0.625, rely=0.05)

    Archivebtn = ttk.Button(Win1, text="Архив задач", command=Archiv)
    Archivebtn.place(relx=0.8, rely=0.05)

    Tasklist = Listbox(Win1)
    Tasklist.place(relx=0, rely=0.15, relwidth=1, relheight=0.9)


# Список для хранения заметок
notes_list = []


def notion():
    Win2 = Tk()
    Win2.title("Заметки")
    Win2.geometry("600x710")
    Win2.resizable(False, False)

    def new_notes():
        # Окно для создания новой заметки
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
        maintext.place(relx=0, rely=0.15, relwidth=1, relheight=0.9)

        def save_note():
            # Сохранение заголовка и текста заметки
            note_title = title.get()
            note_text = maintext.get()

            # Добавляем заголовок в список и отображаем его в Listbox
            if note_title:
                notes_list.append((note_title, note_text))
                Tasklist.insert("end", note_title)

            # Закрываем окно создания заметки
            Nnotes.destroy()

        # Кнопка для сохранения заметки
        save_btn = ttk.Button(Nnotes, text="Сохранить", command=save_note)
        save_btn.place(relx=0.4, rely=0.93)

    def read_note():
        # Получаем выбранную заметку
        selected_index = Tasklist.curselection()
        if selected_index:
            selected_index = selected_index[0]
            note_title, note_text = notes_list[selected_index]

            # Открываем окно для отображения заметки
            ReadNote = Tk()
            ReadNote.title(f"Чтение: {note_title}")
            ReadNote.geometry("600x710")
            ReadNote.resizable(False, False)

            label1 = ttk.Label(ReadNote, text=note_title, font=("Helvetica", 16))
            label1.pack(pady=10)

            label2 = ttk.Label(ReadNote, text=note_text, wraplength=500, justify="left")
            label2.pack(pady=10)

        else:
            showwarning("Ошибка", "Выберите заметку для чтения")

    Createbtn = ttk.Button(Win2, text="Создать", command=new_notes)
    Createbtn.place(relx=0)

    Readbtn = ttk.Button(Win2, text="Читать", command=read_note)
    Readbtn.place(relx=0.4)

    Delbtn = ttk.Button(Win2, text="Удалить")
    Delbtn.place(relx=0.845)

    # Listbox для отображения заголовков заметок
    Tasklist = Listbox(Win2)
    Tasklist.place(relx=0, rely=0.05, relwidth=1, relheight=1)

    Win2.mainloop()


Mainwindow = Tk()
Mainwindow.title("Main menu")  # Титл
Mainwindow.geometry("600x710")  # Разрешние
Mainwindow.resizable(False, False)

Text = ttk.Label(text="Tast Manager", font=("Helvetica", 16))
Text.place(relx=0.426, rely=0.35)

btn = ttk.Button(text="Напоминания", command=windown1)
btn.place(relx=0, y=550, width=600, height=50)

btn1 = ttk.Button(text="Заметки", command=notion)
btn1.place(relx=0, y=620, width=600, height=50)

Mainwindow.mainloop()
