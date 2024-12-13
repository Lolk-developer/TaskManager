from tkinter import *
from tkinter import ttk, filedialog, Toplevel
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
from datetime import date
import json


def windown1():  # Напоминания
    Win1 = Tk()
    Win1.title("Напоминания")
    Win1.geometry("600x710")
    Win1.resizable(False, False)

    def create_task():  # Create task
        task = Createtask.get()
        if task != "":
            Tasklist.insert(0, task)
            with open("tasks.txt", "w") as file:
                file.write(task + "\n")
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, введите напоминание.")

    def edit_win():
        global redact
        task = Tasklist.curselection()

        def update_task():
            Tasklist.delete(task)
            Tasklist.insert(task, Updtask.get())
            Win3.destroy()

        if task:
            Win3 = Tk()
            Win3.title("Редактирование задачи")
            Win3.geometry("500x200")
            Updtask = ttk.Entry(Win3, width=65)
            Updtask.insert(0, Tasklist.get(task))
            Updtask.place(relx=0.1, rely=0.3)
            Updbtn = ttk.Button(Win3, text="Сохранить", command=update_task)
            Updbtn.place(relx=0.42, rely=0.6)
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, ввыберете упоминание!")

    def delete_task():
        task = Tasklist.curselection()
        if task:
            Tasklist.delete(task)
            with open("tasks.txt", "w", encoding='utf-8') as file:
                for item in Tasklist.get(0, END):
                    file.write(item + '\n')
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, ввыберете упоминание!")

    def Archiv():
        global archiv
        Win2 = Tk()
        Win2.title("Архив")
        Win2.geometry("500x600")
        archiv = Listbox(Win2)
        with open("archiv.txt", "r", encoding='utf-8') as file:
            lst = file.readlines()
        for item in lst:
            archiv.insert(END, item)
        archiv.place(relx=0, rely=0, relwidth=1, relheight=0.9)
        DelArch = ttk.Button(Win2, text="Удалить", command=delete_Archiv)
        DelArch.place(relx=0.420, rely=0.9)

    def delete_Archiv():
        global ark
        ark = archiv.curselection()
        if ark:
            archiv.delete(ark)
            with open("archiv.txt", "w", encoding='utf-8') as file:
                for item in archiv.get(0, END):
                    file.write(item + '\n')
        else:
            showerror(title="Пустое поле.", message="Пожалуйста, выберите упоминание!")

    def end_task():
        task = Tasklist.curselection()
        if task:
            Archiv()
            select_task = Tasklist.get(task)
            archiv.insert(END, select_task)
            Tasklist.delete(task)

            with open('archiv.txt', 'a') as file:
                file.write(select_task + '\n')
            with open("tasks.txt", "w", encoding='utf-8') as file:
                for item in Tasklist.get(0, END):
                    file.write(item + '\n')
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
    with open("tasks.txt", "r", encoding='utf-8') as file:
        lst = file.readlines()
    for item in lst:
        Tasklist.insert(0, item)

    scrollbar = ttk.Scrollbar(orient="vertical", command=Tasklist.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

notes_list = []

def save_notes_to_file():
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes_list, file, ensure_ascii=False, indent=4)


def load_notes_from_file():
    global notes_list
    try:
        with open("notes.json", "r", encoding="utf-8") as file:
            notes_list = json.load(file)
    except FileNotFoundError:
        notes_list = []


def notion():
    Win2 = Tk()
    Win2.title("Заметки")
    Win2.geometry("600x710")
    Win2.resizable(False, False)

    def new_notes():
        Nnotes = Tk()
        Nnotes.title("Создание новой заметки")
        Nnotes.geometry("700x810")
        Nnotes.resizable(False, False)


        def add_img():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
            if file_path:
                photos.insert("end", file_path)

        def show_img():
            selected_index = photos.curselection()
            if selected_index:
                file_path = photos.get(selected_index[0])
                img = Image.open(file_path)
                img.show()
            else:
                showerror(title="Пустое поле.", message="Пожалуйста, выберите фото!")

        def delete_img():
            selected_index = photos.curselection()
            if selected_index:
                photos.delete(selected_index[0])


        label1 = ttk.Label(Nnotes, text="Заголовок")
        label1.place(relx=0)

        title = ttk.Entry(Nnotes)
        title.place(relx=0, rely=0.025, relwidth=1)

        tag = ttk.Label(Nnotes, text="Теги")
        tag.place(relx=0, rely=0.08)

        tags = ttk.Entry(Nnotes)
        tags.place(relx=0, rely=0.1, relwidth=1)

        label3 = ttk.Label(Nnotes, text="Текст")
        label3.place(relx=0, rely=0.15)

        maintext = Text(Nnotes)
        maintext.place(relx=0, rely=0.17, relwidth=1, relheight=0.5)

        photos = Listbox(Nnotes)
        photos.place(relx=0, rely=0.7, relwidth=0.75, relheight=0.23)

        addphoto = ttk.Button(Nnotes, text="Добавить фото", command=add_img)
        addphoto.place(relx=0.765, rely=0.695)

        showphoto = ttk.Button(Nnotes, text="Предпросмотр", command=show_img)
        showphoto.place(relx=0.765, rely=0.795)

        deletephoto = ttk.Button(Nnotes, text=" Удалить фото ", command=delete_img)
        deletephoto.place(relx=0.765, rely=0.9)


        def save_note():
            note_title = f"{title.get()} | ({date.today()})"
            note_text = maintext.get("1.0", "end")
            tags_text = tags.get()
            file_paths = photos.get(0, "end")

            if note_title:
                notes_list.append((note_title, note_text, tags_text, file_paths))
                NoteList.insert("end", note_title)
                save_notes_to_file()  
            Nnotes.destroy()

        save_btn = ttk.Button(Nnotes, text="Сохранить", command=save_note)
        save_btn.place(relx=0.4, rely=0.95)


    def read_note():
        selected_index = NoteList.curselection()
        if selected_index:
            selected_index = selected_index[0]
            note_title, note_text, tags, image_paths = notes_list[selected_index]

            ReadNote = Toplevel()
            ReadNote.title(f"{note_title}")
            ReadNote.geometry("600x710")

            label1 = ttk.Label(ReadNote, text=note_title, font=("Helvetica", 16))
            label1.pack(pady=10)

            label2 = ttk.Label(ReadNote, text=f"теги: {tags}", wraplength=500, justify="left")
            label2.pack(pady=10)

            label3 = ttk.Label(ReadNote, text=note_text, wraplength=500, justify="left")
            label3.pack(pady=10)

            images = []

            for i, path in enumerate(image_paths):
                img = Image.open(path)
                img = img.resize((400, 300))
                photo = ImageTk.PhotoImage(img)
                images.append(photo)
                showimg = ttk.Label(ReadNote, image=photo)
                showimg.pack(pady=10)

            ReadNote.images = images
        else:
            showerror("Ошибка", "Выберите заметку для чтения")


    def update_note():
        selected_index = NoteList.curselection()
        if selected_index:
            index = selected_index[0]
            note_title, note_text, tags, image_paths = notes_list[index]

            Rnotes = Tk()
            Rnotes.title("Редактирование заметки")
            Rnotes.geometry("600x710")
            Rnotes.resizable(False, False)


            def add_img():
                file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
                if file_path:
                    newphotos.insert("end", file_path)

            def show_img():
                selected_index = newphotos.curselection()
                if selected_index:
                    file_path = newphotos.get(selected_index[0])
                    img = Image.open(file_path)
                    img.show()
                else:
                    showerror(title="Пустое поле.", message="Пожалуйста, выберите фото!")

            def delete_img():
                selected_index = newphotos.curselection()
                if selected_index:
                    newphotos.delete(selected_index[0])


            label1 = ttk.Label(Rnotes, text="Заголовок")
            label1.place(relx=0)

            newtitle = ttk.Entry(Rnotes)
            newtitle.place(relx=0, rely=0.025, relwidth=1)
            newtitle.insert(0, note_title.split("|")[0])

            tag = ttk.Label(Rnotes, text="Теги")
            tag.place(relx=0, rely=0.08)

            newtags = ttk.Entry(Rnotes)
            newtags.place(relx=0, rely=0.1, relwidth=1)
            newtags.insert(0, tags)

            label3 = ttk.Label(Rnotes, text="Текст")
            label3.place(relx=0, rely=0.15)

            newtext = Text(Rnotes)
            newtext.place(relx=0, rely=0.17, relwidth=1, relheight=0.5)
            newtext.insert("1.0", note_text)

            newphotos = Listbox(Rnotes)
            newphotos.place(relx=0, rely=0.7, relwidth=0.75, relheight=0.23)

            for path in image_paths:
                newphotos.insert("end", path)


            addphoto = ttk.Button(Rnotes, text="Добавить фото", command=add_img)
            addphoto.place(relx=0.765, rely=0.695)

            showphoto = ttk.Button(Rnotes, text="Предпросмотр", command=show_img)
            showphoto.place(relx=0.765, rely=0.795)

            deletephoto = ttk.Button(Rnotes, text=" Удалить фото ", command=delete_img)
            deletephoto.place(relx=0.765, rely=0.9)

            def save_note():
                note_title = f"{newtitle.get()} | ({date.today()})"
                note_text = newtext.get("1.0", "end")
                tags_text = newtags.get()
                file_paths = newphotos.get(0, "end")

                if note_title:
                    notes_list[index] = note_title, note_text, tags_text, file_paths
                    NoteList.delete(selected_index)
                    NoteList.insert(index, note_title)
                    save_notes_to_file()
                Rnotes.destroy()

            save_btn = ttk.Button(Rnotes, text="Сохранить", command=save_note)
            save_btn.place(relx=0.4, rely=0.95)

    def delete_note():
        selected_index = NoteList.curselection()
        if selected_index:
            selected = selected_index[0]
            notes_list.pop(selected)
            NoteList.delete(selected_index)
            save_notes_to_file() 
        else:
            showerror("Ошибка", "Выберите заметку для удаления")
    def tagSearch():
        task = FindTag.get()
        Ntag = Tk()
        idex = []
        idk=0
        Ntag.title("Результат по поиску")
        Ntag.geometry("500x510")
        TagList = Listbox(Ntag)

        def read_note2():
            selected_index = TagList.curselection()
            if selected_index:
                selected_index = selected_index[0]
                note_title, note_text, tags, image_paths = notes_list[idex[selected_index]]

                ReadNote = Toplevel()
                ReadNote.title(f"{note_title}")
                ReadNote.geometry("600x710")

                label1 = ttk.Label(ReadNote, text=note_title, font=("Helvetica", 16))
                label1.pack(pady=10)

                label2 = ttk.Label(ReadNote, text=f"теги: {tags}", wraplength=500, justify="left")
                label2.pack(pady=10)

                label3 = ttk.Label(ReadNote, text=note_text, wraplength=500, justify="left")
                label3.pack(pady=10)

                images = []

                for i, path in enumerate(image_paths):
                    img = Image.open(path)
                    img = img.resize((400, 300))
                    photo = ImageTk.PhotoImage(img)
                    images.append(photo)
                    showimg = ttk.Label(ReadNote, image=photo)
                    showimg.pack(pady=10)

                ReadNote.images = images
            else:
                showerror("Ошибка", "Выберите заметку для чтения")

        def delete_note2():
            selected_index = TagList.curselection()
            if selected_index:
                selected = selected_index[0]
                notes_list.pop(idex[selected])
                TagList.delete(selected_index)
                NoteList.delete(idex[selected])
                save_notes_to_file()
            else:
                showerror("Ошибка", "Выберите заметку для удаления")

        Readbtn2 = ttk.Button(Ntag, text="Читать", command=read_note2)
        Readbtn2.place(relx=0.42)

        Delbtn2 = ttk.Button(Ntag, text="Удалить", command=delete_note2)
        Delbtn2.place(relx=0.845)

        EditBtn2 = ttk.Button(Ntag, text="Изменить")
        EditBtn2.place(relx=0.60)


        TagList.place(relx=0, rely=0.05, relwidth=1, relheight=0.85)
        for note_title, note_text, tags, image_paths in notes_list:
            if tags.find(task)!=-1:
                idex.append(idk)
                TagList.insert("end", note_title)
            idk += 1

        

        Readbtn2 = ttk.Button(Ntag, text="Читать", command=read_note2)
        Readbtn2.place(relx=0.42)

        Delbtn2 = ttk.Button(Ntag, text="Удалить", command=delete_note2)
        Delbtn2.place(relx=0.845)

        EditBtn2 = ttk.Button(Ntag, text="Изменить")
        EditBtn2.place(relx=0.60)


        TagList.place(relx=0, rely=0.05, relwidth=1, relheight=0.85)
        for note_title, note_text, tags, image_paths in notes_list:
            if tags.find(task)!=-1:
                idex.append(idk)
                TagList.insert("end", note_title)
            idk += 1



    Createbtn = ttk.Button(Win2, text="Создать", command=new_notes)
    Createbtn.place(relx=0)

    Readbtn = ttk.Button(Win2, text="Читать", command=read_note)
    Readbtn.place(relx=0.42)

    Delbtn = ttk.Button(Win2, text="Удалить", command=delete_note)
    Delbtn.place(relx=0.845)

    EditBtn = ttk.Button(Win2, text="Изменить", command=update_note)
    EditBtn.place(relx=0.60)

    FindTag = ttk.Entry(Win2)
    FindTag.place(rely=0.94, relx=0.1, width=300)

    LabelTag = ttk.Label(Win2, text="Поиск по тегам:")
    LabelTag.place(relx=0.1, rely=0.91)

    TagButton = ttk.Button(Win2, text="Искать", command=tagSearch)
    TagButton.place(rely=0.937, relx=0.63)

    NoteList = Listbox(Win2)
    NoteList.place(relx=0, rely=0.05, relwidth=1, relheight=0.85)
    load_notes_from_file()
    for note_title, note_text, tags, image_paths in notes_list:
        NoteList.insert("end", note_title)

    scrollbar = ttk.Scrollbar(orient="vertical", command=NoteList.yview)
    scrollbar.pack(side=RIGHT, fill=Y)


Mainwindow = Tk()
Mainwindow.title("Главное меню")
Mainwindow.geometry("600x710")
Mainwindow.resizable(False, False)

welcometext = ttk.Label(text="Tast Manager", font=("Helvetica", 16))
welcometext.place(relx=0.426, rely=0.35)

btn = ttk.Button(text="Напоминания", command=windown1)
btn.place(relx=0, y=550, width=600, height=50)

btn1 = ttk.Button(text="Заметки", command=notion)
btn1.place(relx=0, y=620, width=600, height=50)

Mainwindow.mainloop()
