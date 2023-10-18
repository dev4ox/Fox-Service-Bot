import sqlite3
# Создание базы данных
def create_db():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            username TEXT,
                            fio TEXT,
                            phone TEXT,
                            email TEXT,
                            sub_pub BOOLEAN,
                            reg_date TEXT
                        )
                        ''')
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS orders (
                            order_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            count INTEGER,
                            order_list TEXT,
                            master TEXT,
                            order_date TEXT
                        )
                        ''')
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS payments (
                            user_id INTEGER PRIMARY KEY,
                            count INTEGER,
                            payment_id TEXT,
                            pay_date TEXT
                        )
                        ''')
    except Exception as e:
        print('Error create db', e)
    finally:
        cursor.close()
        conn.close()