import telebot
import sqlite3
import datetime
import key
import menu
import text

bot = telebot.TeleBot(key.tgtoken)
def bot_start():
    @bot.message_handler(commands=['start'])
    def command_start(message):
        user = [message.from_user.id, message.from_user.first_name]
        bot.send_message(user[0], f'<b>Здравствуйте, {user[1]}</b>\n\n'+text.start, 'html', reply_markup=menu.start())

    @bot.callback_query_handler(func=lambda call: True)
    def callback_process(call):
        pass


    bot.polling(none_stop=True)


def infinity_start():
    try:
        bot_start()
    except Exception as error:
        print(error)
        infinity_start()
infinity_start()