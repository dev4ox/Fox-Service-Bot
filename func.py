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
    11: ['users', 'username'],
    12: ['users', 'fio'],
    13: ['users', 'phone'],
    14: ['users', 'email'],
    15: ['users', 'reg_date'],
    16: ['users', 'ref_code'],
    17: ['users', 'sub_pub'],
    18: ['users', 'first_name']
}

def first_join(user_id, first_name, username, ref_code):
    conn = sqlite3.connect(key.db)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()
    #Если новый пользователь
    if not existing_user:
        if ref_code == '':
            ref_code = 0
        # Получаем текущую дату и время
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Добавляем пользователя в базу данных
        cursor.execute(
            'INSERT INTO users (user_id, username, fio, phone, email, reg_date, ref_code, sub_pub, first_name) '
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (user_id, username, '', '', '', current_date, ref_code, '', first_name))
        conn.commit()
    conn.close()



# Запрос к данным users: 11-username, 12-fio, 13-phone, 14-email, 15-reg_date, 16-ref_code, 17-sub_pub, 18-first_name
def db_req_users(user_id: int, parametr: list[int]):
    answer = []
    conn = sqlite3.connect(key.db)
    cursor = conn.cursor()
    try:
        for i in parametr:
            cursor.execute(f"SELECT {KEY_REQUESTS[i][1]} FROM {KEY_REQUESTS[i][0]} WHERE user_id=?", (user_id,))
            result = cursor.fetchone()
            answer.append(result[0])
    except Exception as e:
        print('db_req_users', e)
    finally:
        cursor.close()
        return answer

