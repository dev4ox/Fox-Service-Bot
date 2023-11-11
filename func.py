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
    19: ['users', 'num_orders'],
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

t_now = lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
len_catalog: int = 0
page_max: int = 1


# Первый вход (первая запись в БД)
def first_join(user_id, username, ref_code):
    conn = sqlite3.connect(key.db)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
        existing_user = cursor.fetchone()
        # Если новый пользователь
        if not existing_user:
            if ref_code == '':
                ref_code = 0
            # Добавляем пользователя в базу данных
            cursor.execute(
                "INSERT INTO users (user_id, username, first_name, last_name, phone, email, reg_date, ref_code, "
                "sub_pub, num_orders) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (user_id, username, '-', '-', '-', '-', t_now(), ref_code, 0, 0))
            conn.commit()
    except Exception as e:
        print('"first_join"', e)
    finally:
        conn.close()


# Читает записи в таблице, используя ключи
def db_r_one(user_id: int, parametr: list[int]):
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
        print('"db_r_one"', e)
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
        print('"db_r_last":', e)
    finally:
        conn.close()


# История заказов пользователя return(max_page, [id, master, count])
def user_history(user_id: int):
    conn = sqlite3.connect(key.db)
    try:
        # cursor = conn.execute(f"SELECT order_id, count FROM orders WHERE user_id=? BETWEEN {1} AND {10}", (user_id,))
        cursor = conn.execute(f"SELECT order_id, master, count FROM orders WHERE user_id=?", (user_id,))
        result = cursor.fetchall()
        len_user_h = len(result)
        result.insert(0, (len_user_h - 1) // 10 + 1)
        return result
    except Exception as e:
        print('"user_history":', e)
    finally:
        conn.close()


# Обновление каталога из файла excel
def db_catalog_u():
    conn = sqlite3.connect(key.db)
    try:
        wb = openpyxl.load_workbook(key.catalog)
        sheet = wb.active
        list_catalog = []
        for row in sheet.iter_rows():
            i = [cell.value for cell in row]
            if type(i[0]) is int:
                list_catalog.append(i)
        wb.close()
        global len_catalog, page_max
        len_catalog = len(list_catalog)
        page_max = (len_catalog - 1) // 10 + 1
        conn.execute('DELETE FROM catalog')
        for item_id, name, count in list_catalog:
            conn.execute("INSERT INTO catalog (item_id, name, count) VALUES (?, ?, ?)", (item_id, name, count))
        conn.commit()
        return 'Каталог успешно обновлён', len_catalog
    except Exception as e:
        print('"catalog_u"', e)
        return 'Ошибка обновления', 0
    finally:
        conn.close()


def db_catalog_r(page: str):
    conn = sqlite3.connect(key.db)
    try:
        page = int(page)
        result = []
        cur = conn.cursor()
        if page > 1:
            out_ids = [int(str(page - 1) + '1'), int(str(page) + '0')]
        else:
            out_ids = [1, 10]
        cur.execute(f"SELECT item_id, name, count FROM catalog WHERE item_id BETWEEN {out_ids[0]} AND {out_ids[1]}")
        rows = cur.fetchall()
        for row in rows:
            result.append(row)
        return result
    except Exception as e:
        print('"catalog_r"', e)
    finally:
        conn.close()


# Записывает новый заказ (Смотрит на последний заказ в таблице)
def db_w_new_order(user_data: list):
    conn = sqlite3.connect(key.db)
    try:
        cursor = conn.execute("SELECT * FROM orders ORDER BY order_id DESC LIMIT 1")
        order_id = cursor.fetchone()[0] + 1
        cursor.execute("INSERT INTO orders (order_id, user_id, count, discount, master, order_list, order_date) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?)", (order_id, user_data[0], user_data[1], user_data[2],
                                                        user_data[3], user_data[4], t_now()))
        conn.commit()
        return f'Новый заказ оформлен\n<b>id-заказа: {order_id}</b>'
    except Exception as e:
        print('"db_w_orders"', e)
        return '<b>Ошибка</b>\nПроверьте правильность введённых данных'
    finally:
        conn.close()
