import sqlite3
''' Создание базы данных (database.db)
1 таблица (users):
- id-пользователя (ключ):int,
- ник пользователя:str,
- ФИО:str,
- номер телефона (+79001234567):str,
- e-mail (example@mail.ru):str,
- подписка на канал:bool,
- дата регистрации:str,
- имя пользователя:str

2 таблица (orders):
- номер заказа (ключ):int,
- id-пользователя:int,
- стоимость заказа:int,
- список оказанных услуг (чистка, установка):str,
- мастер, который работал (ФИО):str,
- % скидки:int,
- дата выполнения заказа:str

3 таблица (payments):
- id-пользователя (ключ):int,
- стоимость заказа:int,
- id-платежа:str,
- дата оплаты:str
'''
name = input('Введите название для базы данных: ')
if name == '':
    name = 'database'
try:
    conn = sqlite3.connect(name +'.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        phone TEXT,
                        email TEXT,
                        reg_date TEXT,
                        ref_code TEXT,
                        sub_pub BOOLEAN)''')
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS orders (
                        order_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        count INTEGER,
                        discount INTEGER,
                        master TEXT,
                        order_list TEXT,
                        order_date TEXT)''')
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS payments (
                        pay_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        count INTEGER,
                        pay_date TEXT,
                        trans_id TEXT)''')
    print('База данных "' + name +'.sqlite" успешно создана')
except Exception as e:
    print('Error create db\n', e)
finally:
    cursor.close()
    conn.close()