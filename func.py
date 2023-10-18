from telebot import types
import sqlite3
import telebot
import os
import key
import random
import requests
import json
import datetime


def first_join(user_id, name, code):
    conn = sqlite3.connect('base_ts.sqlite')
    cursor = conn.cursor()
    row = cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"').fetchall()

    ref_code = code
    if ref_code == '':
        ref_code = 0

    if len(row) == 0:
        cursor.execute(
            f'INSERT INTO users VALUES ("{user_id}", "{name}", "{datetime.datetime.now()}", "{user_id}", "{ref_code}", "0")')
        conn.commit()

def create_db():
    conn