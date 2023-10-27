from telebot import types
import sqlite3
import telebot
import os
import key
import random
import requests
import json
import datetime

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
    34: ['payments', 'trans_id']
}


def first_join(user_id, username, ref_code):
    conn = sqlite3.connect(key.db)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()
    # Если новый пользователь
    if not existing_user:
        if ref_code == '':
            ref_code = 0
        # Получаем текущую дату и время
        now_d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        # Добавляем пользователя в базу данных
        cursor.execute(
            'INSERT INTO users (user_id, username, first_name, last_name, phone, email, reg_date, ref_code, sub_pub) '
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (user_id, username, '', '', '', '', now_d, ref_code, ''))
        conn.commit()
    conn.close()


# Запрос к данным через ключи
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
        print('db_req_users', e)
    finally:
        conn.close()


def db_r_last(user_id: int, table: str):
    conn = sqlite3.connect(key.db)
    try:
        cursor = conn.execute(f"SELECT * FROM {table} WHERE user_id=? ORDER BY order_id DESC LIMIT 1", (user_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print('db_req_users', e)
        return None
    finally:
        conn.close()


def db_w_orders(user_id: int, count: int, order_list: str, master: str, discount: int):
    conn = sqlite3.connect(key.db)
    try:
        cursor = conn.cursor()
        now_d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        order_id = int(db_r_last(user_id, 'orders')[0])
        if not order_id:
            order_id = 1
        else:
            order_id += 1
        conn.execute(f"INSERT INTO orders (order_id, user_id, count, order_list, master, discount, order_date) "
                     f"VALUES (?, ?, ?, ?, ?, ?, ?)", (order_id, user_id, count, order_list, master, discount, now_d))
        conn.commit()
    except Exception as e:
        print('db_req_users', e)
    finally:
        conn.close()
