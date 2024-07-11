from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox
from databse import *
import re


def add_user():
    new_name = new_name_textbox.get()
    new_password = new_password_textbox.get()
    if status_combo.get() == 'Администратор':
        new_status = 1
    else:
        new_status = 2
    if all(i.isdigit() for i in new_password) and new_password != '':
        if all(i.isalpha() or i == ' ' for i in new_name) and new_name != '':
            if check_admin_unique(new_status):
                add_user_d(new_name, new_password, new_status)
                messagebox.showinfo('Добавление', 'Новый пользователь добавлен')
            else:
                messagebox.showerror('Ошибка', 'Всего может быть не более одного администратора.')
        else:
            messagebox.showerror('Оишбка', 'Имя пользователя должно содержать только буквы и не может быть пустым.')
    else:
        messagebox.showerror('Оишбка', 'Пароль должен содержать только цифры и не может быть пустым.')


def check_enter():
    user_name = name_combo.get()
    entered_password = password_textbox.get()
    if user_name != '' and entered_password != '':
        user_password = check_user_password(user_name)
        if str(user_password) == entered_password:
            main_window_user(get_userID(user_name))
        else:
            messagebox.showerror('Оишбка', 'Имя пользователя и пароль не совпадают.')
    else:
        messagebox.showerror('Оишбка', 'Имя пользователя и пароль не могут быть пустыми.')


def show_table(tab, flag):
    table = ttk.Treeview(tab)
    table['columns'] = ('id', 'value', 'date', 'category', 'user')
    table.column("#0", width=0, stretch=NO)
    table.column("id", anchor=CENTER, width=30)
    table.column("value", anchor=CENTER, width=90)
    table.column("date", anchor=CENTER, width=100)
    table.column("category", anchor=CENTER, width=180)
    table.column("user", anchor=CENTER, width=230)
    table.heading("#0", text="", anchor=CENTER)
    table.heading("id", text="ID", anchor=CENTER)
    table.heading("value", text="Значение", anchor=CENTER)
    table.heading("date", text="Дата", anchor=CENTER)
    table.heading("category", text="Категория", anchor=CENTER)
    table.heading("user", text="Пользователь", anchor=CENTER)
    if flag:
        data = get_incomes()
    else:
        data = get_expenses()
    for i in range(len(data)):
        table.insert(parent='', index='end', iid=i, text='', values=data[i])
    return table


def show_table_moneybox(tab):
    table = ttk.Treeview(tab)
    table['columns'] = ('id', 'value', 'date', 'user')
    table.column("#0", width=0, stretch=NO)
    table.column("id", anchor=CENTER, width=30)
    table.column("value", anchor=CENTER, width=80)
    table.column("date", anchor=CENTER, width=90)
    table.column("user", anchor=CENTER, width=220)
    table.heading("#0", text="", anchor=CENTER)
    table.heading("id", text="ID", anchor=CENTER)
    table.heading("value", text="Значение", anchor=CENTER)
    table.heading("date", text="Дата", anchor=CENTER)
    table.heading("user", text="Пользователь", anchor=CENTER)
    data = get_remittance()
    for i in range(len(data)):
        table.insert(parent='', index='end', iid=i, text='', values=data[i])
    return table


def add_income(userID):
    income_window = Tk()
    income_window.title('Добавить запись')
    income_window.geometry('400x325')
    income_window.resizable(False, False)
    income_window.focus_set()
    income_window.grab_set()

    value_label = Label(income_window, text='Значение', font=('Arial Bold', 15))
    value_label.place(x=30, y=50)
    value_textbox = Entry(income_window, width=23)
    value_textbox.place(x=200, y=50)

    date_label = Label(income_window, text='Дата', font=('Arial Bold', 15))
    date_label.place(x=30, y=120)
    date_textbox = Entry(income_window, width=23)
    date_textbox.place(x=200, y=120)

    category_label = Label(income_window, text='Категория', font=('Arial Bold', 15))
    category_label.place(x=30, y=190)
    category_combo = Combobox(income_window)
    category_combo['values'] = get_categories_i()
    category_combo.place(x=200, y=190)

    def insert_income():
        value = value_textbox.get()
        date = date_textbox.get()
        category = category_combo.get()
        if value != '' and date != '' and category != '':
            if all(i.isdigit() for i in value):
                date_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
                if date_regex.match(date):
                    add_income_values(userID, value, date, category)
                    messagebox.showinfo('Добавление', 'Новая запись добавлена')
                    income_window.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Неверный формат даты. (Правильный: "yyyy-mm-dd")')
            else:
                messagebox.showerror('Ошибка', 'Введено неверное значение.')
        else:
            messagebox.showerror('Ошибка', 'Все поля должны быть заполнены (значение, дата, категория).')

    add_button = Button(income_window, text="Пополнить", height=3, width=20, command=insert_income)
    add_button.place(x=110, y=250)

    income_window.mainloop()


def add_expense(userID):
    expense_window = Tk()
    expense_window.title('Добавить запись')
    expense_window.geometry('400x325')
    expense_window.resizable(False, False)
    expense_window.focus_set()
    expense_window.grab_set()

    value_label = Label(expense_window, text='Значение', font=('Arial Bold', 15))
    value_label.place(x=30, y=50)
    value_textbox = Entry(expense_window, width=23)
    value_textbox.place(x=200, y=50)

    date_label = Label(expense_window, text='Дата', font=('Arial Bold', 15))
    date_label.place(x=30, y=120)
    date_textbox = Entry(expense_window, width=23)
    date_textbox.place(x=200, y=120)

    category_label = Label(expense_window, text='Категория', font=('Arial Bold', 15))
    category_label.place(x=30, y=190)
    category_combo = Combobox(expense_window)
    category_combo['values'] = get_categories_e()
    category_combo.place(x=200, y=190)

    def insert_expense():
        value = value_textbox.get()
        date = date_textbox.get()
        category = category_combo.get()
        if value != '' and date != '' and category != '':
            if all(i.isdigit() for i in value):
                date_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
                if date_regex.match(date):
                    add_expense_values(userID, value, date, category)
                    messagebox.showinfo('Добавление', 'Новая запись добавлена')
                    expense_window.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Неверный формат даты. (Правильный: "yyyy-mm-dd")')
            else:
                messagebox.showerror('Ошибка', 'Введено неверное значение.')
        else:
            messagebox.showerror('Ошибка', 'Все поля должны быть заполнены (значение, дата, категория).')

    add_button = Button(expense_window, text="Заплатить", height=3, width=20, command=insert_expense)
    add_button.place(x=110, y=250)

    expense_window.mainloop()


def add_moneybox(userID, flag):
    moneybox_window = Tk()
    moneybox_window.title('Добавить запись')
    moneybox_window.geometry('400x325')
    moneybox_window.resizable(False, False)
    moneybox_window.focus_set()

    value_label = Label(moneybox_window, text='Значение', font=('Arial Bold', 15))
    value_label.place(x=30, y=50)
    value_textbox = Entry(moneybox_window, width=23)
    value_textbox.place(x=200, y=50)

    date_label = Label(moneybox_window, text='Дата', font=('Arial Bold', 15))
    date_label.place(x=30, y=120)
    date_textbox = Entry(moneybox_window, width=23)
    date_textbox.place(x=200, y=120)

    def insert_remittance():
        value = value_textbox.get()
        date = date_textbox.get()
        if value != '' and date != '':
            if all(i.isdigit() for i in value):
                date_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
                if date_regex.match(date):
                    add_moneybox_values(userID, value, date, flag)
                    messagebox.showinfo('Добавление', 'Новая запись добавлена')
                    moneybox_window.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Неверный формат даты. (Правильный: "yyyy-mm-dd")')
            else:
                messagebox.showerror('Ошибка', 'Введено неверное значение.')
        else:
            messagebox.showerror('Ошибка', 'Все поля должны быть заполнены (значение, дата, категория).')

    if flag:
        add_button = Button(moneybox_window, text="Внести", height=3, width=20, command=insert_remittance)
        add_button.place(x=110, y=250)
    else:
        add_button = Button(moneybox_window, text="Снять", height=3, width=20, command=insert_remittance)
        add_button.place(x=110, y=250)

    moneybox_window.mainloop()


def change_category(flag):
    new_category_window = Tk()
    new_category_window.title('Новая категория')
    new_category_window.geometry('400x200')
    new_category_window.resizable(False, False)
    new_category_window.focus_set()

    title_label = Label(new_category_window, text='Название', font=('Arial Bold', 15))
    title_label.place(x=50, y=50)
    title_entry = Entry(new_category_window, width=15)
    title_entry.place(x=200, y=55)

    def add_category():
        title = title_entry.get()
        if title != '':
            add_new_category(title, flag)
            messagebox.showinfo('Добавление', f'Категория "{title}" добавлена.')
            new_category_window.destroy()
        else:
            messagebox.showerror('Ошибка', 'Название категории не указано.')

    add_button = Button(new_category_window, text="Добавить", height=2, width=15, command=add_category)
    add_button.place(x=50, y=130)

    def delete_category():
        title = title_entry.get()
        if title != '':
            if (title in get_categories_i() and flag is False) or \
                    (title in get_categories_e() and flag is True):
                delete_category_i_e(title, flag)
                messagebox.showinfo('Удаление', f'Категория "{title}" удалена.')
                new_category_window.destroy()
            else:
                messagebox.showerror('Ошибка', 'Категории с таким названием не найдено.')
        else:
            messagebox.showerror('Ошибка', 'Название категории не указано.')

    delete_button = Button(new_category_window, text="Удалить", height=2, width=15, command=delete_category)
    delete_button.place(x=220, y=130)

    new_category_window.mainloop()


def update_operation(flag):
    update_window = Tk()
    update_window.title('Изменить запись')
    update_window.geometry('400x325')
    update_window.resizable(False, False)
    update_window.focus_set()
    update_window.grab_set()

    id_label = Label(update_window, text='ID', font=('Arial Bold', 10))
    id_label.place(x=30, y=35)
    id_combo = Combobox(update_window)
    id_combo['values'] = get_ID(flag)
    id_combo.place(x=200, y=35)

    value_label = Label(update_window, text='Значение', font=('Arial Bold', 10))
    value_label.place(x=30, y=90)
    value_textbox = Entry(update_window, width=15)
    value_textbox.place(x=200, y=90)

    date_label = Label(update_window, text='Дата', font=('Arial Bold', 10))
    date_label.place(x=30, y=145)
    date_textbox = Entry(update_window, width=15)
    date_textbox.place(x=200, y=145)

    category_label = Label(update_window, text='Категория', font=('Arial Bold', 10))
    category_label.place(x=30, y=200)
    category_combo = Combobox(update_window)
    if not flag:
        category_combo['values'] = get_categories_i()
    else:
        category_combo['values'] = get_categories_e()
    category_combo.place(x=200, y=200)

    def update():
        id = id_combo.get()
        value = value_textbox.get()
        date = date_textbox.get()
        category = category_combo.get()
        if id != '' and value != '' and date != '' and category != '':
            if all(i.isdigit() for i in value):
                date_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
                if date_regex.match(date):
                    update_i_e(id, value, date, category, flag)
                    messagebox.showinfo('Изменение', f'Операция изменена (ID={id})')
                    update_window.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Неверный формат даты. (Правильный: "yyyy-mm-dd")')
            else:
                messagebox.showerror('Ошибка', 'Введено неверное значение.')
        else:
            messagebox.showerror('Ошибка', 'Все поля должны быть заполнены (ID, значение, дата, категория).')

    add_button = Button(update_window, text="Изменить", height=3, width=20, command=update)
    add_button.place(x=110, y=250)

    change_category_button = Button(update_window, text="\\", height=1, width=3, command=lambda: change_category(flag))
    change_category_button.place(x=355, y=200)

    update_window.mainloop()


def update_moneybox():
    moneybox_window = Tk()
    moneybox_window.title('Изменить запись')
    moneybox_window.geometry('400x325')
    moneybox_window.resizable(False, False)
    moneybox_window.focus_set()
    moneybox_window.grab_set()

    id_label = Label(moneybox_window, text='ID', font=('Arial Bold', 10))
    id_label.place(x=30, y=35)
    id_combo = Combobox(moneybox_window)
    id_combo['values'] = get_ID_r()
    id_combo.place(x=200, y=35)

    value_label = Label(moneybox_window, text='Значение', font=('Arial Bold', 10))
    value_label.place(x=30, y=90)
    value_textbox = Entry(moneybox_window, width=15)
    value_textbox.place(x=200, y=90)

    date_label = Label(moneybox_window, text='Дата', font=('Arial Bold', 10))
    date_label.place(x=30, y=145)
    date_textbox = Entry(moneybox_window, width=15)
    date_textbox.place(x=200, y=145)

    def update():
        id = id_combo.get()
        value = value_textbox.get()
        date = date_textbox.get()
        if value != '' and date != '' and id != '':
            if all(i.isdigit() for i in value) or value[0] == '-' and all(i.isdigit() for i in value[1:]):
                date_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
                if date_regex.match(date):
                    update_r(id, value, date)
                    messagebox.showinfo('Изменение', f'Операция изменена (ID={id})')
                    moneybox_window.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Неверный формат даты. (Правильный: "yyyy-mm-dd")')
            else:
                messagebox.showerror('Ошибка', 'Введено неверное значение.')
        else:
            messagebox.showerror('Ошибка', 'Все поля должны быть заполнены (ID, значение, дата).')

    add_button = Button(moneybox_window, text="Изменить", height=3, width=20, command=update)
    add_button.place(x=110, y=250)

    moneybox_window.mainloop()


def delete_operation(flag):
    delete_window = Tk()
    delete_window.title('Удалить запись')
    delete_window.geometry('400x200')
    delete_window.resizable(False, False)
    delete_window.focus_set()
    delete_window.grab_set()

    id_label = Label(delete_window, text='ID записи', font=('Arial Bold', 15))
    id_label.place(x=50, y=50)
    id_combo = Combobox(delete_window)
    if flag == 0:
        id_combo['values'] = get_ID(0)
    elif flag == 1:
        id_combo['values'] = get_ID(1)
    else:
        id_combo['values'] = get_ID_r()
    id_combo.place(x=200, y=55)

    def delete_o():
        id = id_combo.get()
        if id != '':
            delete_i_e_r(id, flag)
            messagebox.showinfo('Удаление', f'Операция удалена (ID={id}).')
            delete_window.destroy()
        else:
            messagebox.showerror('Ошибка', 'ID операции не указан.')

    add_button = Button(delete_window, text="Удалить", height=2, width=15, command=delete_o)
    add_button.place(x=115, y=130)

    delete_window.mainloop()


def main_window_user(userID):
    first_window.destroy()
    main_window = Tk()
    main_window.title('Домашние финансы')
    main_window.geometry('800x450')
    main_window.resizable(False, False)
    main_window.focus_set()

    main_control = ttk.Notebook(main_window)
    budget = ttk.Frame(main_control)
    incomes = ttk.Frame(main_control)
    expenses = ttk.Frame(main_control)
    momeybox = ttk.Frame(main_control)
    main_control.add(budget, text='Баланс')
    main_control.add(incomes, text='Доходы')
    main_control.add(expenses, text='Расходы')
    main_control.add(momeybox, text='Копилка')

    balance_label_text = Label(budget, text='Баланс', font=('Arial Bold', 25))
    balance_label_text.pack(side=TOP, pady=40)
    balance_label = Entry(budget, font=('Arial Bold', 25), justify='center')
    balance_label.insert(END, get_balance())
    balance_label.pack(side=TOP, pady=50)

    def set_text_by_button():
        balance_label.delete(0, "end")
        balance_label.insert(0, get_balance())
    balance_button = Button(budget, text="Обновить", height=3, width=20, command=set_text_by_button)
    balance_button.pack(anchor=S, pady=50)

    income_label = Label(incomes, text='Поступления', font=('Arial Bold', 30))
    income_label.pack(side=TOP, pady=30)
    add_income_button = Button(incomes, text="Пополнить", height=3, width=20, command=lambda: add_income(userID))
    add_income_button.place(x=180, y=350)
    income_table = show_table(incomes, True)
    income_table.pack()

    def refresh_incomes():
        nonlocal income_table
        income_table.destroy()
        income_table = show_table(incomes, True)
        income_table.pack()

    income_table_button = Button(incomes, text="Обновить", height=3, width=20, command=refresh_incomes)
    income_table_button.place(x=440, y=350)
    if get_user_status(userID) == 1:
        income_update_button = Button(incomes, text="\\", height=1, width=3,
                                      command=lambda: update_operation(False))
        income_update_button.place(x=730, y=120)
        income_delete_button = Button(incomes, text="x", height=1, width=3,
                                      command=lambda: delete_operation(0))
        income_delete_button.place(x=730, y=150)

    expense_label = Label(expenses, text='Затраты', font=('Arial Bold', 30))
    expense_label.pack(side=TOP, pady=30)
    add_expense_button = Button(expenses, text="Заплатить", height=3, width=20, command=lambda: add_expense(userID))
    add_expense_button.place(x=180, y=350)
    expense_table = show_table(expenses, False)
    expense_table.pack()

    def refresh_expenses():
        nonlocal expense_table
        expense_table.destroy()
        expense_table = show_table(expenses, False)
        expense_table.pack()

    expense_table_button = Button(expenses, text="Обновить", height=3, width=20, command=refresh_expenses)
    expense_table_button.place(x=440, y=350)
    if get_user_status(userID) == 1:
        expense_update_button = Button(expenses, text="\\", height=1, width=3,
                                       command=lambda: update_operation(True))
        expense_update_button.place(x=730, y=120)
        expense_delete_button = Button(expenses, text="x", height=1, width=3,
                                       command=lambda: delete_operation(1))
        expense_delete_button.place(x=730, y=150)

    moneybox_label = Label(momeybox, text='Баланс копилки', font=('Arial Bold', 25))
    moneybox_label.place(x=80, y=30)
    moneybox_textbox = Entry(momeybox, font=('Arial Bold', 20), justify='center')
    moneybox_textbox.insert(END, get_balance_r())
    moneybox_textbox.place(x=40, y=150)
    moneybox_table = show_table_moneybox(momeybox)
    moneybox_table.place(x=370, y=30)

    def set_text_by_button_r():
        moneybox_textbox.delete(0, "end")
        moneybox_textbox.insert(0, get_balance_r())

        nonlocal moneybox_table
        moneybox_table.destroy()
        moneybox_table = show_table_moneybox(momeybox)
        moneybox_table.place(x=370, y=30)

    balance_button = Button(momeybox, text="Обновить", height=3, width=20, command=set_text_by_button_r)
    balance_button.place(x=100, y=250)

    add_moneybox_button = Button(momeybox, text="Пополнить", height=3, width=20,
                                 command=lambda: add_moneybox(userID, True))
    add_moneybox_button.place(x=400, y=350)
    take_moneybox_button = Button(momeybox, text="Снять", height=3, width=20,
                                  command=lambda: add_moneybox(userID, False))
    take_moneybox_button.place(x=600, y=350)
    if get_user_status(userID) == 1:
        moneybox_update_button = Button(momeybox, text="\\", height=1, width=3,
                                        command=lambda: update_moneybox())
        moneybox_update_button.place(x=330, y=220)
        moneybox_delete_button = Button(momeybox, text="x", height=1, width=3,
                                        command=lambda: delete_operation(2))
        moneybox_delete_button.place(x=330, y=250)

    main_control.pack(expand=1, fill='both')
    main_window.mainloop()


first_window = Tk()
first_window.title("Вход/регистрация")
first_window.geometry('800x450')
first_window.resizable(False, False)
first_window.focus_set()

tab_control = ttk.Notebook(first_window)
enter = ttk.Frame(tab_control)
registration = ttk.Frame(tab_control)
tab_control.add(enter, text='Вход')
tab_control.add(registration, text='Регистрация')


hello_label = Label(enter, text="Добро пожаловать", font=("Arial Bold", 30))
hello_label.pack(side=TOP, pady=20)
name_label = Label(enter, text="Пользователь", font=("Arial Bold", 15))
name_label.place(x=120, y=170)
password_label = Label(enter, text="Пароль", font=("Arial Bold", 15))
password_label.place(x=120, y=225)
name_combo = Combobox(enter)
name_combo['values'] = get_users()
name_combo.place(x=500, y=170)


def update_name_combo():
    global name_combo
    name_combo['values'] = get_users()


update_name = Button(enter, text="[]", height=1, width=3, command=update_name_combo)
update_name.place(x=700, y=170)
password_textbox = Entry(enter, width=23)
password_textbox.place(x=500, y=227)
enter_button = Button(enter, text="Вход", height=3, width=20, command=check_enter)
enter_button.pack(side=BOTTOM)

registration_label = Label(registration, text="Регистрация", font=("Arial Bold", 30))
registration_label.pack(side=TOP, pady=20)
new_name_label = Label(registration, text="ФИО", font=("Arial Bold", 15))
new_name_label.place(x=140, y=160)
new_name_textbox = Entry(registration, width=23)
new_name_textbox.place(x=500, y=160)
new_password_label = Label(registration, text="Пароль", font=("Arial Bold", 15))
new_password_label.place(x=140, y=205)
new_password_textbox = Entry(registration, width=23)
new_password_textbox.place(x=500, y=205)
status_label = Label(registration, text="Статус", font=("Arial Bold", 15))
status_label.place(x=140, y=250)
status_combo = Combobox(registration)
status_combo['values'] = ('Пользователь', 'Администратор')
status_combo.place(x=500, y=250)
new_user_button = Button(registration, text="Добавить", height=3, width=20, command=add_user)
new_user_button.pack(side=BOTTOM)

tab_control.pack(expand=1, fill='both')
first_window.mainloop()


if connection:
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")

