import sqlite3
info = ''' Создание базы данных ({}.db)
1 таблица (users):
- id-пользователя (ключ):int,
- ник пользователя:str,
- имя:str,
- фамилия:str,
- номер телефона (+79001234567):str,
- e-mail (example@mail.ru):str,
- дата регистрации:str,
- реферальный код:str,
- подписка на канал:bool

2 таблица (orders):
- номер заказа (ключ):int,
- id-пользователя:int,
- стоимость заказа:int,
- скидка (1-100):int,
- мастер, который работал (фио):str,
- список оказанных услуг (чистка, установка):str,
- дата выполнения заказа:str

3 таблица (payments):
- id-платежа (ключ):int,
- id-пользователя:int,
- стоимость:int,
- дата оплаты:str,
- id-транзакции (в платёжке):str
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
    print(info.format(name))
    print('\n База данных "' + name + '.sqlite" успешно создана')
except Exception as e:
    print('Error create db\n', e)
finally:
    cursor.close()
    conn.close()