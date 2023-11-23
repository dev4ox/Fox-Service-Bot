import sqlite3

info = '''
1 таблица (users):
- (KEY) id-пользователя:int,
- ник пользователя:str,
- имя:str,
- фамилия:str,
- номер телефона (+79001234567):str,
- e-mail (example@mail.ru):str,
- дата регистрации:str,
- реферальный код:str,
- подписка на канал:bool,
- количество заказов:int

2 таблица (orders):
- (KEY) id-заказа:int,
- id-пользователя:int,
- стоимость заказа:int,
- скидка (1-100):int,
- мастер, который работал (фио):str,
- список оказанных услуг (чистка, установка):str,
- дата выполнения заказа:str

3 таблица (payments):
- (KEY) id-заказа, оплаченный:int,
- id-пользователя:int,
- стоимость:int,
- дата оплаты:str,
- id-транзакции (в платёжке):str

4 таблица (catalog):
- (KEY) id-услуги:int,
- название услуги:str,
- стоимость услуги:int
'''

name = input('Введите название для базы данных: ')
if name == '':
    name = 'database'
conn = sqlite3.connect(name + '.sqlite')
try:
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
                        sub_pub BOOLEAN,
                        num_orders INTEGER)''')
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
                        order_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        count INTEGER,
                        pay_date TEXT,
                        trans_id TEXT)''')
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS catalog (
                        item_id INTEGER PRIMARY KEY,
                        name TEXT,
                        count INTEGER)''')
    cursor.execute(f"INSERT INTO orders (order_id, user_id, count, discount, master, order_list, order_date) "
                   f"VALUES (?, ?, ?, ?, ?, ?, ?)", (0, 0, 0, 0, 0, 0, 0))
    conn.commit()
    print(info)
    print('База данных "' + name + '.sqlite" успешно создана')
except Exception as e:
    print('Error create db\n', e)
finally:
    conn.close()
