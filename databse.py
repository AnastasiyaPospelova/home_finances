import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Fuckingpassword1",
                              host="127.0.0.1",
                              port="5432",
                              database="kursach")
cursor = connection.cursor()
cursor.execute('SET search_path TO home_finance,public')


def check_admin_unique(status):
    if status == 2:
        return True
    else:
        sql = 'SELECT ID_status FROM users'
        cursor.execute(sql)
        users_statuses = tuple(i[0] for i in cursor.fetchall())
        if status not in users_statuses:
            return True
        else:
            return False


def add_user_d(new_name, new_password, status):
    sql = 'INSERT INTO users (FIO, ID_status, user_password)'\
          f'VALUES (\'{new_name}\', {status}, {new_password})'
    cursor.execute(sql)
    connection.commit()


def check_user_password(user_FIO):
    sql = f'SELECT user_password FROM users WHERE FIO = \'{user_FIO}\''
    cursor.execute(sql)
    return cursor.fetchone()[0]


def get_balance():
    sql = 'SELECT balance FROM budget'
    cursor.execute(sql)
    return cursor.fetchone()[0]


def get_balance_r():
    sql = 'SELECT SUM(value_r) FROM moneybox'
    cursor.execute(sql)
    return cursor.fetchone()[0]


def get_users():
    sql = 'SELECT FIO FROM users'
    cursor.execute(sql)
    users = tuple(i[0] for i in cursor.fetchall())
    return users


def get_user_status(userID):
    sql = 'SELECT ID_status FROM users ' \
          f'WHERE ID_user = {userID}'
    cursor.execute(sql)
    return int(cursor.fetchone()[0])


def get_categories_i():
    sql = 'SELECT title FROM categories_i'
    cursor.execute(sql)
    categories_i = tuple(i[0] for i in cursor.fetchall())
    return categories_i


def get_categories_e():
    sql = 'SELECT title FROM categories_e'
    cursor.execute(sql)
    categories_e = tuple(i[0] for i in cursor.fetchall())
    return categories_e


def delete_category_i_e(title, flag):
    if not flag:
        sql = f"DELETE FROM categories_i WHERE id_category = (" \
              f"SELECT id_category WHERE title = '{title}')"
    else:
        sql = f"DELETE FROM categories_e WHERE id_category = (" \
              f"SELECT id_category WHERE title = '{title}')"
    cursor.execute(sql)
    connection.commit()


def get_userID(userFIO):
    sql = f'SELECT ID_user FROM users WHERE FIO = \'{userFIO}\''
    cursor.execute(sql)
    return int(cursor.fetchone()[0])


def get_incomes():
    sql = 'SELECT ID_income, value_i, date_i, title, FIO FROM incomes ' \
          'INNER JOIN categories_i USING(ID_category) ' \
          'INNER JOIN users USING(ID_user)'
    cursor.execute(sql)
    return cursor.fetchall()


def get_expenses():
    sql = 'SELECT ID_expence, value_e, date_e, title, FIO FROM expences ' \
          'INNER JOIN categories_e USING(ID_category) ' \
          'INNER JOIN users USING(ID_user)'
    cursor.execute(sql)
    return cursor.fetchall()


def get_remittance():
    sql = 'SELECT ID_remittance, value_r, date_r, FIO FROM moneybox ' \
          'INNER JOIN users USING(ID_user)'
    cursor.execute(sql)
    return cursor.fetchall()


def get_ID(flag):
    if not flag:
        sql = 'SELECT ID_income FROM incomes'
    else:
        sql = 'SELECT ID_expence FROM expences'
    cursor.execute(sql)
    return cursor.fetchall()


def get_ID_r():
    sql = 'SELECT ID_remittance FROM moneybox'
    cursor.execute(sql)
    return cursor.fetchall()


def add_new_category(title, flag):
    if not flag:
        sql = f"INSERT INTO categories_i (title) VALUES ('{title}')"
    else:
        sql = f"INSERT INTO categories_e (title) VALUES ('{title}')"
    cursor.execute(sql)
    connection.commit()


def add_income_values(ID_user, value_i, date_i, title):
    sql = f'SELECT ID_category FROM categories_i WHERE title = \'{title}\''
    cursor.execute(sql)
    ID_category = int(cursor.fetchone()[0])
    sql = 'INSERT INTO incomes(ID_user, value_i, date_i, ID_category) ' \
          f'VALUES ({ID_user}, {value_i}, \'{date_i}\', {ID_category})'
    cursor.execute(sql)
    connection.commit()


def add_expense_values(ID_user, value_e, date_e, title):
    sql = f'SELECT ID_category FROM categories_e WHERE title = \'{title}\''
    cursor.execute(sql)
    ID_category = int(cursor.fetchone()[0])
    sql = 'INSERT INTO expences(ID_user, value_e, date_e, ID_category) ' \
          f'VALUES ({ID_user}, {value_e}, \'{date_e}\', {ID_category})'
    cursor.execute(sql)
    connection.commit()


def add_moneybox_values(ID_user, value_r, date_r, flag):
    if flag:
        sql = 'INSERT INTO moneybox(ID_user, value_r, date_r) '\
              f'VALUES ({ID_user}, {value_r}, \'{date_r}\')'
    else:
        sql = 'INSERT INTO moneybox(ID_user, value_r, date_r) ' \
              f'VALUES ({ID_user}, {-int(value_r)}, \'{date_r}\')'
    cursor.execute(sql)
    connection.commit()


def update_i_e(id, value, date, category, flag):
    if not flag:
        sql = f'SELECT ID_category FROM categories_i WHERE title = \'{category}\''
        cursor.execute(sql)
        ID_category = int(cursor.fetchone()[0])
        sql = f"UPDATE incomes SET (value_i, date_i, ID_category) = ({value}, '{date}', '{ID_category}') " \
              f"WHERE ID_income = {id}"
    else:
        sql = f'SELECT ID_category FROM categories_e WHERE title = \'{category}\''
        cursor.execute(sql)
        ID_category = int(cursor.fetchone()[0])
        sql = f"UPDATE expences SET (value_e, date_e, ID_category) = ({value}, '{date}', '{ID_category}') " \
              f"WHERE ID_expence = {id}"
    cursor.execute(sql)
    connection.commit()


def update_r(id, value, date):
    sql = f"UPDATE moneybox SET (value_r, date_r) = ({value}, '{date}') " \
          f"WHERE ID_remittance = {id}"
    cursor.execute(sql)
    connection.commit()


def delete_i_e_r(id, flag):
    if not flag:
        sql = f"DELETE FROM incomes WHERE ID_income = {id}"
    elif flag == 1:
        sql = f"DELETE FROM expences WHERE ID_expence = {id}"
    else:
        sql = f"DELETE FROM moneybox WHERE ID_remittance = {id}"
    cursor.execute(sql)
    connection.commit()
