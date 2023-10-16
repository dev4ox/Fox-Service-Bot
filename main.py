import telebot
import sqlite3
import datetime
import key

bot = telebot.TeleBot(key.tgtoken)
def bot_start():
    pass


def infinity_start():
    try:
        bot_start()
    except:
        infinity_start()
infinity_start()