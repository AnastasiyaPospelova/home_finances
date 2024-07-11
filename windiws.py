from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox

def show_window():
    main_window = Tk()
    main_window.title("Вход/регистрация")
    main_window.geometry('800x450')
    main_window.configure(bg='lightyellow')

    tab_control = ttk.Notebook(main_window)
    enter = ttk.Frame(tab_control)
    registration = ttk.Frame(tab_control)
    tab_control.add(enter, text='Вход')
    tab_control.add(registration, text='Регистрация')

    hello_label = Label(enter, text="Добро пожаловать", font=("Arial Bold", 30))
    hello_label.pack(side=TOP, pady=20)
    name_label = Label(enter, text="Пользователь", font=("Arial Bold", 15))
    name_label.place(x=120, y=170)
    status_label = Label(enter, text="Статус", font=("Arial Bold", 15))
    status_label.place(x=120, y=225)
    name_combo = Combobox(enter)
    name_combo['values'] = (1, 2, 3, 4, 5)
    name_combo.place(x=500, y=170)
    status_combo = Combobox(enter)
    status_combo['values'] = (1, 2, 3, 4, 5)
    status_combo.place(x=500, y=225)

    tab_control.pack(expand=1, fill='both')

    main_window.mainloop()

# def clicked():
#     pass
    # messagebox.showinfo('Заголовок', 'Текст')
    # messagebox.showwarning('Заголовок', 'Текст')
    # messagebox.showerror('Заголовок', 'Текст')
    # messagebox.askquestion('Заголовок', 'Текст')
    # messagebox.askyesno('Заголовок', 'Текст')
    # messagebox.askyesnocancel('Заголовок', 'Текст')
    # messagebox.askokcancel('Заголовок', 'Текст')
    # messagebox.askretrycancel('Заголовок', 'Текст')

# tab_control = ttk.Notebook(window)
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
# tab_control.add(tab1, text='Первая')
# tab_control.add(tab2, text='Вторая')
#
# lbl = Label(tab1, text="Привет")
# lbl.grid(column=0, row=0)
# txt = Entry(tab1, width=10)
# txt.grid(column=1, row=0)
# btn = Button(tab2, text="Клик!", command=clicked)
# btn.grid(column=2, row=0)
# combo = Combobox(tab1)
# combo['values'] = (1, 2, 3, 4, 5)
# combo.current(0)  # установите вариант по умолчанию
# combo.grid(column=3, row=0)
# #Чтобы получить элемент select, можно использовать функцию combo.get()
# tab_control.pack(expand=1, fill='both')
