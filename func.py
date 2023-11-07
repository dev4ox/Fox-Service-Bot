import sqlite3
import datetime
import key
import openpyxl

KEY_REQUESTS = {
    10: ['users', 'user_id'],
    11: ['users', 'username'],
    12: ['users', 'first_name'],
    13: ['users', 'last_name'],
    14: ['users', 'phone'],
    15: ['users', 'email'],
    16: ['users', 'reg_date'],
    17: ['users', 'ref_code'],
    18: ['users', 'sub_pub'],
    20: ['orders', 'order_id'],
    21: ['orders', 'user_id'],
    22: ['orders', 'count'],
    23: ['orders', 'order_list'],
    24: ['orders', 'master'],
    25: ['orders', 'discount'],
    26: ['orders', 'order_date'],
    30: ['payments', 'pay_id'],
    31: ['payments', 'user_id'],
    32: ['payments', 'count'],
    33: ['payments', 'pay_date'],
    34: ['payments', 'trans_id'],
    40: ['catalog', 'item_id'],
    41: ['catalog', 'name'],
    42: ['catalog', 'count']
}

t_now = lambda: datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


def first_join(user_id, username, ref_code):
    conn = sqlite3.connect(key.db)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()
    # Если новый пользователь
    if not existing_user:
        if ref_code == '':
            ref_code = 0
        # Добавляем пользователя в базу данных
        cursor.execute(
            'INSERT INTO users (user_id, username, first_name, last_name, phone, email, reg_date, ref_code, sub_pub) '
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (user_id, username, '-', '-', '-', '-', t_now(), ref_code, '0'))
        conn.commit()
    conn.close()


# Чтение данных, используя ключи
def db_r(user_id: int, parametr: list[int]):
    answer = []
    conn = sqlite3.connect(key.db)
    try:
        cursor = conn.cursor()
        for i in parametr:
            cursor.execute(f"SELECT {KEY_REQUESTS[i][1]} FROM {KEY_REQUESTS[i][0]} WHERE user_id=?", (user_id,))
            result = cursor.fetchone()
            answer.append(result[0])
        return answer
    except Exception as e:
        print('db_r', e)
    finally:
        conn.close()


# Читает последнюю запись в БД
def db_r_last(user_id: int, table: str):
    conn = sqlite3.connect(key.db)
    try:
        cursor = conn.execute(f"SELECT * FROM {table} WHERE user_id=? ORDER BY order_id DESC LIMIT 1", (user_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print('db_r_last:', e)
    finally:
        conn.close()


# Записывает новый заказ (Смотрит на последний заказ в таблице)
def db_w_new_order(user_id: int, count: int, discount: int, order_list: str, master: str):
    conn = sqlite3.connect(key.db)
    try:
        cursor = conn.execute(f"SELECT * FROM orders ORDER BY order_id DESC LIMIT 1")
        order_id = cursor.fetchone()[0] + 1
        cursor.execute(f"INSERT INTO orders (order_id, user_id, count, discount, master, order_list, order_date) "
                       f"VALUES (?, ?, ?, ?, ?, ?, ?)", (order_id, user_id, count, discount, order_list, master,
                                                         t_now()))
        conn.commit()
    except Exception as e:
        print('db_w_orders', e)
    finally:
        conn.close()


# Обновление каталога из файла excel
def update_catalog():
    try:
        wb = openpyxl.load_workbook(key.catalog)
        sheet = wb.active
        list_catalog = []
        for row in sheet.iter_rows():
            i = [cell.value for cell in row]
            if type(i[0]) is int:
                list_catalog.append(i)
        wb.close()
        # list_catalog.insert(0, len(list_catalog))
        conn = sqlite3.connect(key.db)
        for item_id, name, count in list_catalog:
            conn.execute(f"INSERT INTO catalog (item_id, name, count) VALUES (?, ?, ?)", (item_id, name, count))
        conn.commit()
        return 'Каталог успешно обновлён'
    except Exception as e:
        print('update_catalog', e)
        return 'Ошибка обновления'